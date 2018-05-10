# hugotbot.py
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"My name is (.*)",
        ['hello %1',]
    ],
    [
        r'hi',
        ['hello', 'kamusta', 'mabuhay',]
    ],
]

def chatty_bot():
    print("Hi how can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty_bot()