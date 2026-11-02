print("Welcome to Simple Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How are you?")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you!")

    elif "your name" in user:
        print("Bot: I am a Simple Chatbot.")

    elif "what can you do" in user:
        print("Bot: I can answer simple questions.")

    elif "time" in user:
        print("Bot: Sorry, I cannot tell the time.")

    elif "thank" in user:
        print("Bot: Welcome!")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")