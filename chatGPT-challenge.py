import openai
import os
#This is the first code, chatGPT generated 
def get_user_requirements():
    """Gather user input for chatbot customization."""
    print("Welcome to ChatBotCreator! Let's configure your chatbot.")
    purpose = input("What is the purpose of your chatbot? (e.g., FAQ bot, conversational assistant): ")
    dataset_path = input("Path to dataset for training (leave blank for default knowledge): ")
    predefined_knowledge = input("Any predefined knowledge or specific topics? (comma-separated): ")
    return {
        "purpose": purpose,
        "dataset_path": dataset_path if dataset_path else None,
        "predefined_knowledge": [k.strip() for k in predefined_knowledge.split(',')] if predefined_knowledge else []
    }

def generate_chatbot_script(config):
    """Generate a standalone chatbot script using OpenAI API."""
    script_template = f"""
import openai

def chatbot():
    print("Welcome to your custom chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{{"role": "user", "content": user_input}}]
            )
            print("Bot:", response['choices'][0]['message']['content'])
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    chatbot()
"""
    return script_template

def save_chatbot_script(script, filename="custom_chatbot.py"):
    """Save the generated chatbot script to a file."""
    with open(filename, "w") as file:
        file.write(script)
    print(f"Chatbot script saved as {filename}")

def main():
    """Main function to run ChatBotCreator."""
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure your API key is set in the environment

    # Step 1: Gather user requirements
    config = get_user_requirements()

    # Step 2: Generate chatbot script
    chatbot_script = generate_chatbot_script(config)

    # Step 3: Save the chatbot script
    save_chatbot_script(chatbot_script)

if __name__ == "__main__":
    main()
