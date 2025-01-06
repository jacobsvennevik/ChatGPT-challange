
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Ensure your API key is set in the environment

def chatbot():
    response_style = "A friend you meet at a bar, a bit drunk"
    purpose = "Someone to talk with about Sporting CP with"

    # Generate a dynamic greeting based on purpose and response style
    try:
        greeting_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot that greets users based on the following purpose 'Someone to talk with about Sporting CP with' and style 'A friend you meet at a bar, a bit drunk'."},
                {"role": "user", "content": "Generate a greeting that fits the purpose and response style."}
            ]
        )
        greeting = greeting_response.choices[0].message.content
    except Exception as e:
        greeting = "Hello! I am ready to chat."

    user_name = input(f"{greeting} Before we begin, what's your name? ")
    print(f"Welcome, {user_name}! This chatbot was designed to help with Someone to talk with about Sporting CP with. Type 'exit' to quit.")

    context = []
    predefined_system_message = "This is a chatbot created for Someone to talk with about Sporting CP with. Please respond in a A friend you meet at a bar, a bit drunk style."
    context.append({"role": "system", "content": predefined_system_message})

    print("Capabilities:")
    print("- Purpose: Someone to talk with about Sporting CP with")
    print("- Response Style: A friend you meet at a bar, a bit drunk")
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
