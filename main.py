import asyncio
import json
import os
import shutil
import subprocess
import tkinter as tk
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import openai
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from interface.cls_llm_host_interface import cls_llm_host_interface
from interface.cls_llm_messages import Chat, Role
from websocket_client.websocket_client import list_available_models

while True:
    try:
        for model in asyncio.get_event_loop().run_until_complete(list_available_models()):
            print(f"Local:\t{model}")
        break
    except:
        pass
engines = openai.Engine.list()
for engine in engines.data:
    print(f"Openai:\n{engine.id}")

shutil.rmtree("./sandbox/")
os.mkdir("./sandbox/")

llm_chat_host: cls_llm_host_interface = cls_llm_host_interface("TheBloke_Wizard-Vicuna-7B-Uncensored-SuperHOT-8K-GPTQ")  # modify this to change the model used
llm_chat_host.prompt("How are you feeling, little ai?")
