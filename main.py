# chatty_bot
# Examples: https://github.com/nltk/nltk/tree/develop/nltk/chat
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"My name is (.*)",
        ["Hello %1"]
    ],
    [
        r"Hi",
        ["Hello", "Hi", "Hey",]
    ],
    [
        r"(.*) your name?",
        ["Peter"]
    ],
    [
        r"(.*)", # default response if no patterns from above is found
        ["Sorry I don't know what `%1` is?"]
    ]
]

def chatty_bot():
    print("Hi how can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty_bot()