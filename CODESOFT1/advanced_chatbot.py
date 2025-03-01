import re

class RuleBasedChatBot:
    def __init__(self):
        self.patterns = {
            r'\b(hi|hello|hey)\b': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!"
            ],
            r'how are you': [
                "I'm doing great, thanks for asking!",
                "I'm wonderful! How are you?",
                "All good here! How about you?"
            ],
            r'what.*your name': [
                "I'm ChatBot, your friendly AI assistant!",
                "You can call me ChatBot!",
                "ChatBot is my name!"
            ],
            r'(bye|goodbye)': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Come back soon!"
            ],
            r'(thank|thanks)': [
                "You're welcome!",
                "Glad I could help!",
                "My pleasure!"
            ]
        }
        
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "That's interesting! Tell me more.",
            "I'm still learning about that topic."
        ]
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                return responses[0]  # You could randomize this choice
        
        return self.default_responses[0]

def main():
    chatbot = RuleBasedChatBot()
    print("ChatBot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
            
        response = chatbot.get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
