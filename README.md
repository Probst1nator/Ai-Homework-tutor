# Welcome to the (Local)-Language-Model-Toolkit

Welcome to the (Local)-Language-Model-Toolkit, an open-source framework designed to serve as a foundation for building advanced language model tools. Whether you're a seasoned developer or a newcomer eager to automate tasks requiring contextual understanding, this project is tailored to your needs.

# Getting Started

## 1. Install the Required Dependencies

Before you begin, make sure to install the necessary dependencies listed in the `requirements.txt` file. You can do this using `pip`. Open your terminal or command prompt, navigate to the project directory, and run the following command:
```cmd
pip install -r requirements.txt
```

This command will install all the required packages for your project.

## 2. Configure Environment

1. Rename `.env.example` to `.env`.
2. Insert the path of your local language models (e.g., `..\text-generation-webui-main\models`) and/or insert your OpenAI token.

## 3. Start the Local Language Model Server

Manually launch the `llm.api.py` to run in the background and serve local language models.

## 4. Run Your Project

Run your project by executing the `main.py` file (ensure `llm.api.py` is active for local LLM support). This will print out all available models (local and OpenAI).

## 5. Customize Project

To develop a custom project, it's recommended to begin by implementing and experimenting in the `main.py` file.
Pick a model, by inserting its name into the "cls_llm_host_interface" class!

# Contributing

I'd love to hear what you think about this project! Dive in, propose/(commit) changes, or simply share your thoughts. Feedback is highly encouraged.

# License

This project is open source and is provided as-is. You are free to use it at your discretion. Please review the LICENSE file for more details.


Enjoy!
