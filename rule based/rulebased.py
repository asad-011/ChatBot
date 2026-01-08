def chatbot():
    print("Bot: Hello! I am your chatbot")
    print("Bot: Type 'bye' to exit.")

    name = ""

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hi! How can I help you?")

        elif user in ["what is your name", "who are you"]:
            print("Bot: I am a simple Python chatbot.")

        elif user.startswith("my name is"):
            name = user.replace("my name is", "").strip()
            print(f"Bot: Nice to meet you, {name}!")

        elif user in ["what is my name", "do you know my name"]:
            if name:
                print(f"Bot: Yes, your name is {name}.")
            else:
                print("Bot: I don't know your name yet.")

        elif user in ["how are you", "how r u"]:
            print("Bot: I'm doing great! Thanks for asking ")
        
        elif user == "help":
            print("Bot: You can ask me things like:")
            print("     - hello")
            print("     - my name is Asad")
            print("     - what is your name")
            print("     - tell me a joke")
            print("     - time")
            print("     - bye")

        elif user == "time":
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current time is {current_time}")

        elif user in ["tell me a joke", "joke"]:
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs 😂")

        elif user in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day 👋")
            break

        else:
            print("Bot: Sorry, I didn't understand that. Type 'help'.")

chatbot()
