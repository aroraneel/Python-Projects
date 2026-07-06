# Import load_dotenv() to load environment variables from the .env file
from dotenv import load_dotenv

# HumanMessage represents the message sent by the user to the AI
from langchain_core.messages import HumanMessage

# Import Claude AI model from LangChain
from langchain_anthropic import ChatAnthropic

# Import create_react_agent() to create an AI agent
# Agent = An AI assistant that can think, reason, and use tools to answer questions
from langgraph.prebuilt import create_react_agent

# Import tool decorator from LangChain.
# @tool allows the AI agent to use a Python function as a tool.
from langchain.tools import tool

# Load all variables (like API keys) from the .env file
load_dotenv()

# -------------------- Calculator Tool --------------------

# @tool tells LangChain that this function
# can be called by the AI whenever needed.
@tool
def calculator(a: float, b: float) -> str:
    """
    Use this tool to perform basic arithmetic calculations.

    a: First number
    b: Second number

    Returns the sum of both numbers.
    """

    # Print a message in the terminal whenever
    # the AI uses this tool.
    print("Calculator tool has been called.")

    # Return the result as a formatted string.
    return f"The sum of {a} and {b} is {a + b}"


# -------------------- Greeting Tool --------------------

# @tool tells LangChain that this function
# can also be used by the AI.
@tool
def say_hello(name: str) -> str:
    """
    Use this tool to greet a user by their name.

    name: Name of the user

    Returns a friendly greeting message.
    """

    # Print a message in the terminal whenever
    # the AI uses this tool.
    print("Greeting tool has been called.")

    # Return a personalized greeting.
    return f"Hello {name}, I hope you are well today."

# -------------------- Main Function --------------------

def main():

    # Create the Claude AI model
    # temperature = Controls randomness
    # 0 = More accurate and consistent answers
    # Higher values = More creative but less predictable
    model = ChatAnthropic(
        model="claude-3-5-haiku-latest",
        temperature=0
    )

    # List of tools the AI can use
    # List of tools available for the AI.
    # The AI will automatically choose which tool to use
    # based on the user's request.
    tools = [
        calculator,
        say_hello
    ]

    # Create an AI agent using the Claude model and available tools
    agent_executor = create_react_agent(model, tools)

    # Display welcome message
    print("Welcome to the AI Assistant.")
    print("I'm here to answer your questions and perform calculations.")
    print("Type 'quit' to exit the application.")

    # Run the chatbot continuously
    while True:

        # Take input from the user
        # strip() removes extra spaces from the beginning and end
        user_input = input("\nYou: ").strip()

        # Exit the program if the user types "quit"
        # lower() converts text to lowercase
        # Example: QUIT -> quit
        if user_input.lower() == "quit":
            print("\nGoodbye!")
            break

        # Print Assistant before showing the AI response
        print("\nAssistant: ", end="", flush=True)

        # Send the user's message to the AI
        # stream() returns the response little by little
        # instead of waiting for the complete answer
        for chunk in agent_executor.stream(

            # HumanMessage tells the AI that this message
            # is coming from the user
            {"messages": [HumanMessage(content=user_input)]}
        ):

            # Check if the AI has generated a response
            if "agent" in chunk:

                # Loop through all messages returned by the AI
                for message in chunk["agent"]["messages"]:

                    # Print the AI response immediately
                    # flush=True displays text instantly
                    print(message.content, end="", flush=True)

        # Move to the next line after the response is complete
        print()


# -------------------- Program Entry Point --------------------

# This ensures the main() function runs only
# when this file is executed directly.
# It will not run automatically if this file
# is imported into another Python program.
if __name__ == "__main__":
    main()