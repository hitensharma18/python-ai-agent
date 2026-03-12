import random

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
import os

load_dotenv()
@tool
def addition(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    print("The tool has been called")
    return f"The sum of {a} and {b} is {a+b}"

@tool
def subtract(a: float, b: float) -> str:
    """Subtract two numbers"""
    return f"The difference between {a} and {b} is {a - b}"

@tool
def multiply(a: float, b: float) -> str:
    """Multiply two numbers"""
    return f"The product of {a} and {b} is {a * b}"

@tool
def divide(a: float, b: float) -> str:
    """Divide two numbers"""
    if b == 0:
        return "Cannot divide by zero"
    return f"The result of {a} divided by {b} is {a / b}"

@tool
def power(a: float, b: float) -> str:
    """Raise a number to a power"""
    return f"{a} to the power of {b} is {a ** b}"

import datetime

@tool
def get_time() -> str:
    """Get the current time"""
    return datetime.datetime.now().strftime("%H:%M:%S")

import math

@tool
def square_root(a: float) -> str:
    """Calculate the square root of a number"""
    if a < 0:
        return "Cannot take square root of negative number"
    return f"The square root of {a} is {math.sqrt(a)}"

@tool
def random_number(a: int, b: int) -> str:
    """Generate a random number between two numbers"""
    if a > b:
        return "First number must be smaller than second number"
    num = random.randint(a, b)
    return f"A random number between {a} and {b} is {num}"

@tool
def get_day() -> str:
    """Get the current day"""
    import datetime
    return datetime.datetime.now().strftime("%A")

@tool
def temperature(c: float) -> str:
    """Convert Celsius to Fahrenheit"""
    f = (c * 9/5) + 32
    return f"{c} degrees Celcius = {f} degrees Fahrenheit"
@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user"""
    return f"Hello {name}, i hope you are well today!"

def main():
    model = ChatOpenAI(temperature = 0)

    tools = [addition, subtract, multiply, divide, power, get_time, square_root, random_number, get_day, temperature, say_hello]
    
    memory = MemorySaver()
    agent_executor = create_react_agent(model=model, tools=tools, checkpointer=memory)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to preform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]},
            {"configurable": {"thread_id": "1"}}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
            print()

if __name__ == "__main__":
    main()

        
