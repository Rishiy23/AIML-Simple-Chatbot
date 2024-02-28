import random

# Define basic questiions and their respective answers for the chatbot
basic_questions= {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you?": ["I'm good, thanks!", "I'm doing well, how about you?", "Feeling great, thanks for asking!"],
    "what is your name?": ["I'm your virtual assistant Chatbot", "My name is Chatbot"],
    "how was your day?": ["As usual helping and assisting  others with their queries."],
    "when where you born?": ["I am a software, I wasn't born but created."],
    "farewell": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "error": ["I'm sorry, I didn't understand that.", "Could you please repeat that?"],
}


# Previous context variables
previous_context = {}

# Function to get a response from the chatbot
def get_response(message):
    global previous_conversation
    message = message.lower()

    if message in previous_context:
        response = "You previously asked '"+message+"' and answered '"+previous_context[message]+"'. Is there anything else I can help with?"
        return response
    if "hello" in message or "hi" in message or "hey" in message:
        return random.choice(basic_questions["greeting"])
    elif "bye" in message or "goodbye" in message:
        return random.choice(basic_questions["farewell"])
    elif message in basic_questions:
        response = random.choice(basic_questions[message]) 
        previous_context[message] = response
        return response
    
    else:
        return random.choice(basic_questions["error"])
    
#Asking Questions from the user
def ask_user():
    n = random.randint(3,6)
    l = []
    questions = ["What is your name?", 
                   "What do you do?", 
                   "How are you?", 
                   "How old are you?", 
                   "What is your favourite sport?", 
                   "What is you hobby?"]
    while(n>0):
        print("Chatbot: "+questions[n])
        user_answer = input("You: ")
        n-=1
    
# Main function to run the chatbot
def main():
    print("Chatbot: Hello! Welcome to the chatbot. Ask me anything or type 'exit' to end the conversation.")
    print("Chatbot: First lets have your intro.")
    ask_user()
    print("Chatbot: It was great chatting with you!")
    print("Chatbot: Ask me anything or type 'exit' to end the conversation.")


    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot:", random.choice(basic_questions["farewell"]))
            break
        print("Chatbot:", get_response(user_input))

if __name__ == "__main__":
    main()
