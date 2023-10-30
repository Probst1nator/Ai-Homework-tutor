import json
from enum import Enum
from typing import List, Union


class Role(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Chat:
    def __init__(self, user_message: str, instruction_message: str = ""):
        self.messages: List[tuple[Role, str]] = []
        if instruction_message:
            self.add_message(Role.SYSTEM, instruction_message)
        self.add_message(Role.USER, user_message)

    def add_message(self, role: Role, content: str):
        self.messages.append((role, content))

    def __str__(self):
        return json.dumps([{"role": message[0].value, "content": message[1]} for message in self.messages])

    def to_dict(self):
        return [{"role": message[0].value, "content": message[1]} for message in self.messages]
