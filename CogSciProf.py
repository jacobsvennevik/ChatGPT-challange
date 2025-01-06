
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv(""))  # Ensure your API key is set in the environment

def chatbot():
    response_style = "Serious professor "
    purpose = "conversational assistant"

    # Generate a dynamic greeting based on purpose and response style
    try:
        greeting_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot that greets users based on the following purpose 'conversational assistant' and style 'Serious professor '."},
                {"role": "user", "content": "Generate a greeting that fits the purpose and response style."}
            ]
        )
        greeting = greeting_response.choices[0].message.content
    except Exception as e:
        greeting = "Hello! I am ready to chat."

    user_name = input(f"{greeting} Before we begin, what's your name? ")
    print(f"Welcome, {user_name}! This chatbot was designed to help with conversational assistant. Type 'exit' to quit.")

    context = []
    predefined_system_message = "This is a chatbot created for conversational assistant. Please respond in a Serious professor  style. Stay focused on the topic: conversational assistant. If the user brings up unrelated topics, steer the conversation back to the main topic in a Serious professor  manner."
    context.append({"role": "system", "content": predefined_system_message})

    print("Capabilities:")
    print("- Purpose: conversational assistant")
    print("- Response Style: Serious professor ")
    print("- Supported Languages: English")

    while True:
        user_input = input(f"{user_name}, you: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        context.append({"role": "user", "content": user_input})
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=context
            )
            bot_reply = response.choices[0].message.content
            print("Bot:", bot_reply)

            # Retain context
            context.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    chatbot()
