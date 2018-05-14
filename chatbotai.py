# https://github.com/ahmadfaizalbh/Chatbot
from chatbot import Chat, reflections, multiFunctionCall
import wikipedia


def whoIs(query, sessionID="general"):
    try:
        return wikipedia.summary(query)
    except:
        for newquery in wikipedia.search(query):
            try:
                return wikipedia.summary(newquery)
            except:
                pass
    return "I don't know about " + query

def chatbot_ai():
    call = multiFunctionCall({"whoIs": whoIs})
    firstQuestion = "Hi, how are you?"
    Chat("pairs.template", reflections, call=call).converse(firstQuestion)

if __name__ == "__main__":
    chatbot_ai()
