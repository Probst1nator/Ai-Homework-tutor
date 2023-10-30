import asyncio
import json
import os

import openai
from decouple import config

from interface.cls_llm_messages import Chat, Role
from websocket_client.websocket_client import prompt_model

openai.api_key = config("OPENAI_API_KEY")


class cls_llm_host_interface:
    def __init__(self, model: str):
        self.model = model

    def _get_cached_text_generation(self, chat: Chat, model):
        for entry in self.text_generations:
            if entry.get("messages") == str(chat) and entry.get("model") == model:
                return entry.get("generated_text")
        return None

    def _add_to_cache(self, chat: Chat, model, generated_text):
        self.text_generations.append({"model": model, "messages": str(chat), "generated_text": generated_text})
        with open("./cache/text_generations_cache.json", "w") as json_file:
            json.dump(self.text_generations, json_file, indent=4)

    def _send_prompt(self, chat: Chat, max_new_tokens: int, model="gpt-3.5-turbo") -> str:
        if model != "gpt-3.5-turbo":
            return asyncio.get_event_loop().run_until_complete(self.prompt_model(str(chat), model, max_new_tokens))

        cached_text = self._get_cached_text_generation(chat, model)
        if cached_text is not None:
            print(cached_text)
            return cached_text

        response = openai.ChatCompletion.create(model=model, messages=chat.to_dict(), max_tokens=max_new_tokens)
        generated_text = response.choices[0].message.content
        print(generated_text)

        self._add_to_cache(chat, model, generated_text)

        return generated_text

    def prompt(
        self,
        user_message: str,
        instruction_message: str = "",
        condition_assistant_response: str = "",
        condition_assistant_response_end: str = "",
        max_new_tokens: int = 1024,
    ) -> str:
        chat = Chat(user_message, instruction_message)
        chat.add_message(Role.ASSISTANT, condition_assistant_response)

        response = self._send_prompt(chat, max_new_tokens)

        if "i hope" in response.lower() or "have any questions" in response.lower() or "let me know" in response.lower():
            last_newline_index = response.rfind("\n")
            if last_newline_index != -1:
                response = response[:last_newline_index].strip().strip("\n").strip()

        if condition_assistant_response_end:
            response = response.strip() + f" {condition_assistant_response_end}"
            response = self._send_prompt(response, max_new_tokens)

        return response
