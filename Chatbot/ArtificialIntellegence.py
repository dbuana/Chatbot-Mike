# The seential libraries for ChatBot
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
import json
import nltk
chatbot = ChatBot("Mike")
CCB = ChatterBotCorpusTrainer(chatbot)
# We will be implemeting the .json code into this code, meaning that
# we will have to export attachments

# The main code for chatbot Mike; will include greetings, converstaion, questions on certain things and many more things!

# Greetings; when starting the code greet ChatBot Mike and the ChatBot will learn more about the user
ChatBotGreetings = ChatBot("Mike",
	questions="chatbotAttachments/greetings/patterns.json",
	response="chatbotAttachments/greetings/responses.json",
	mainDatabase="chatbotAttachments/greetings.json"
	)
# current_events; THe information regarding current events
ChatBotEvents = ChatBot("Mike",
 	questions="chatbotAttachments/current_events/patterns.json", 
 	response="chatbotAttachments/current_events/responses.json",
 	mainDatabase="chatbotAttachments/current_events.json"
  	)
# Questions; basically what you ask on a day-to-day conversation
ChatBotQuestions = ChatBot("Mike",
	questions="chatbotAttachments/questions/patterns.json",
	response="chatbotAttachments/questions/responses.json",
	mainDatabase="chatbotAttachments/questions.json"
	)
# THe function will indicate the functionality of the artificial intellegence
def chatBotMike():
	# THe input of chatbot
	chatbotInput = input("")
	anotherQuestion = chatborInput+"?"
	# THe for loop will indicate the outcome of the input
	for c in chatbot:
		if chatbotInput == "Hey!":
			ChatBotGreetings = ChatBot("Mike",
				questions="chatbotAttachments/greetings/patterns.json",
				response="chatbotAttachments/greetings/responses.json",
				mainDatabase="chatbotAttachments/greetings.json"
				) # The process will repeat and later on it will be implemented on a "while loop"
				# Another response in advance
			if chatbotInput == anotherQuestion:
				#anotherResponse = ("Mike",
				#	response="",
				#	)
				pass
		elif chatbotInput == "What?":
			ChatBotEvents = ChatBot("Mike",
				questions="chatbotAttachments/current_events/patterns.json",
				response="chatbotAttachments/current_events/responses.json",
				mainDatabase="chatbotAttachments/current_events.json"
				)
			return ChatBotEvents and True 
		# Adding a while statement
		while  chatbotInput.strip() == "stop":
			print("See you!")
			break
		