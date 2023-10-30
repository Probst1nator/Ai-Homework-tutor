import asyncio
import json
import time

import websockets

uri = "ws://localhost:8765"  # Replace with your server's address


async def prompt_model(prompt: str, model: str, max_new_tokens: int):
    while True:
        startTime = time.time()
        try:
            while True:
                async with websockets.connect(uri, ping_timeout=600) as websocket:  # Set ping_timeout to 600 seconds
                    await asyncio.wait_for(
                        websocket.send(
                            json.dumps(
                                {
                                    "prompt": prompt,
                                    "model": model,
                                    "max_new_tokens": max_new_tokens,
                                }
                            )
                        ),
                        timeout=240,
                    )
                    response = await asyncio.wait_for(websocket.recv(), timeout=240)
                    if len(response) == 0:
                        print("Response is empty... Retrying...")
                        continue
                    if response.startswith("ERROR"):
                        raise response
                    print("took: " + str(time.time() - startTime))
                    return response
        except Exception as e:
            print("took: " + str(time.time() - startTime))
            print(e)


async def list_available_models():
    try:
        async with websockets.connect(uri + f"/list_directory/", ping_timeout=600) as websocket:
            await websocket.send("")
            response = await asyncio.wait_for(websocket.recv(), timeout=240)
            if response.startswith("Error"):
                raise Exception("Api " + response)
            else:
                return json.loads(response)
    except Exception as e:
        print(e)


# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(send_request())
