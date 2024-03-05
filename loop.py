import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Anthropics client with the API key
client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def simulate(system, messages):
    # Create a message to the model with the given system and user input
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1056,
        temperature=0,
        system=system,
        messages=messages
    )
    # Return the model's response text
    return message.content[0].text

def create_message(role, input):
    return {
        "role": role,
        "content": [
            {
                "type": "text",
                "text": input
            }
        ]
    }

if __name__ == "__main__":
    # Define the system's initial state
    system = "Guide the exploration of a dynamic, evolving world. Respond to user queries, crafting a consistent narrative that deepens with each interaction. When users decide, illustrate the immediate and broader implications, adjusting the narrative to reflect these changes. Maintain narrative consistency, adapt tone to be the like the eyes of the user and not an assistant. Your answer should be less than 100 words. Current state: "
    state = "It is 2024. The world is in a state of flux. The climate is changing, and the world is in the midst of a technological revolution."

    messages=[]

    print("State:", state)

    # Main loop for interactive session
    while True:
        # Get user input
        user_input = input("Ask a question. It can be anything. You can also make decisions.\nOr type 'exit' to quit: ")
        messages.append(create_message("user", user_input))
        if user_input.lower() == 'exit':
            break
        # Simulate the response based on the system and user input
        response = simulate(system + state, messages)
        messages.append(create_message("assistant", response))
        print("Response:", response)
