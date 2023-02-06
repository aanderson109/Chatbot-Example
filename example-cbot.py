from chatterbot import chatbot
from chatterbot.trainers import ListTrainer

# creating a new chatbot
chatbot = Chatbot('Parker Contracting, Inc. Customer Service')
trainer = ListTrainer(chatbot)
trainer.train(['Hi, Welcome to the Parker Contracting, Inc. Customer Service Module'])

# getting a response from the chatbot
response = chatbot.get_response("I need help")
print(response)