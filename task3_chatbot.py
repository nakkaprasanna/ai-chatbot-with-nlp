import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["I'm a chatbot."]],
    ["how are you?", ["I'm doing good, how can I help you?"]],
    ["bye", ["Goodbye!", "See you later!"]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
