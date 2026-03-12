AI Agent Assistant with Tools and Memory

An intelligent Python-based AI assistant built using LangChain and LangGraph that can perform arithmetic calculations, provide date and time information, greet users, generate random numbers, and remember past interactions. The assistant is interactive, adaptive, and designed to help automate tasks efficiently.

Features

Performs addition, subtraction, multiplication, division, power, and square root calculations

Converts Celsius to Fahrenheit

Generates random numbers within a given range

Provides current time and day

Greets users with personalized messages

Maintains memory of past interactions for context-aware responses

Built using Python, LangChain, LangGraph, and OpenAI API

Installation

Clone the repository:

git clone https://github.com/hitensharma18/python-ai-agent.git

Navigate into the project folder:

cd python-ai-agent

Create and activate a virtual environment:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Add your OpenAI API key to a .env file:

OPENAI_API_KEY=your_openai_api_key_here
Usage

Run the assistant using:

uv run main.py

Type your commands, ask it to calculate, get the time, or greet someone. Type quit to exit.

Contributing

Contributions are welcome. Please ensure no secrets or API keys are included in commits.

License

Specify your license here (e.g., MIT, Apache 2.0).
