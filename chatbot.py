print("Chatbot: Hi! Type 'quit' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "quit":
        print("Chatbot: Bye!")
        break
    elif "hello" in user_input:
        print("Chatbot: Hey there!")
    else:
        print("Chatbot: I don't understand yet.")

