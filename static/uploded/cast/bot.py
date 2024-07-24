from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

# Create a new chatbot
chatbot = ChatBot("MyChatBot")

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Load data from JSON file
with open("static/uploded/cast/bot.json", "r") as file:
    training_data = json.load(file)

# Train the chatbot with the training data
for data in training_data:
    trainer.train([
        data["text"],
        data["response"]
    ])
exit_conditions = (":q", "quit", "exit")
while True:
    query =  input("> Users responce").capitalize()
    if query in exit_conditions:
        break
    else:
        print(f"Chatbot response :-{chatbot.get_response(query)}")
