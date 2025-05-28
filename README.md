# gemini-multi-turn-chat-saurabh

## Gemini Multi-turn Chatbot

A simple interactive chatbot using Google's Gemini Free API that maintains conversation context across multiple turns.

## Features

- Maintains conversation context across multiple turns
- Adjustable temperature parameter (0.0 to 2.0) for controlling response creativity
- Command support for changing temperature during conversation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Gemini API key from: https://makersuite.google.com/app/apikey

3. Create a `.env` file in the project directory with your API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Run the chatbot:
```bash
python gemini_chatbot.py
```

2. When prompted, enter your desired initial temperature (0.0 to 2.0):
   - 0.0: More deterministic, factual responses
   - 1.0: Balanced creativity and factual responses
   - 2.0: More creative, varied responses
   - Press Enter to use the default temperature (0.7)

3. Start chatting with Gemini!
   - Type your messages and press Enter to send
   - Type 'quit' to end the conversation
   - Use `/set_temp <value>` to change temperature during conversation
     (e.g., `/set_temp 0.9`)

## Temperature Guide

The temperature parameter controls the randomness of the model's responses:
- Lower values (closer to 0.0): More focused, deterministic responses
- Higher values (closer to 2.0): More creative, varied responses
- Default value (0.7): Balanced between creativity and factual accuracy

## Example Conversation

Here's an example of interacting with the chatbot:

```
Enter initial temperature (0.0 to 2.0, default 0.7): 1.0

Welcome to the Gemini Chatbot!
Using model: gemini-1.5-flash-latest
Initial temperature: 1.0
Type '/set_temp <value>' to change temperature (e.g., /set_temp 0.9).
Type 'quit' to end the conversation.

You: what is llm

Gemini: LLM stands for **Large Language Model**.  It's a type of artificial intelligence (AI) that can understand and generate human-like text.  These models are trained on massive amounts of text data, allowing them to learn patterns, grammar, and facts about the world.  This enables them to perform a wide range of tasks, including:

* **Translation:**  Translating text from one language to another.
* **Summarization:**  Condensing large amounts of text into shorter summaries.
* **Question answering:**  Answering questions based on their training data.
* **Text generation:**  Creating different kinds of creative text formats (poems, code, scripts, musical pieces, email, letters, etc.)
* **Chatbots:**  Engaging in conversations with users.

LLMs are built using deep learning techniques, typically involving transformer networks.  Examples of LLMs include GPT-3, LaMDA, and PaLM.


You: what is chat gpt

Gemini: ChatGPT is a large language model chatbot.  It's a specific implementation of an LLM (Large Language Model) developed by OpenAI.  Unlike some other LLMs that might be used for more general tasks, ChatGPT is specifically designed for conversational interactions.  

Key features of ChatGPT include:

* **Conversational ability:**  It's designed to engage in back-and-forth dialogue, remembering previous turns in the conversation to maintain context.
* **Human-like text generation:**  It aims to produce responses that are natural and coherent, mimicking human conversation styles.
* **Adaptability:**  While trained on a massive dataset, it can adapt to different conversation styles and topics.
* **Fine-tuning:**  OpenAI continually refines ChatGPT's capabilities through ongoing training and updates.

Essentially, ChatGPT is a sophisticated chatbot that leverages the power of LLMs to provide engaging and informative conversational experiences.  It's important to remember that while it can generate remarkably human-like text, it doesn't possess genuine understanding or consciousness.  Its responses are based on patterns and relationships learned from its training data.


You: what was my first question

Gemini: Your first question was: "what is llm"


You: quit

Goodbye!
```