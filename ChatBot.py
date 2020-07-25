# ChatBot Mike; version I

# This cahtbot will made with NLTK library
import nltk
from nltk.chat.util import Chat, reflections
import random
import numpy as np
# Creating another AI, using another form of practice
# On the .json file, we have to implement the code into our Python3 code
#name = input("Type in your name: ")

# introduction function
def MikeTheChatbot():
	line = f"Hey! I am Mike your artificial inteligence friend"
	return line
# Coonversation subjects
def ConversationSubject():
	# This function will mostly be dedicated to the conversation subjects of ChatBot Mike
	convo = input("")
	choice1 = "yes"
	choice2 = "switch subject"
	def convo():
		if convo == choice1:
			expected += 1
			pass
		elif convo == choice2:
			response = input("Okay, what else do you want to talk about?")
			for response in convo(1):
				if convo == choice2:
					expected += 1
					pass
				# Finding conversation topics
		topics = input("What would you like to talk about?")
		if topics == "":
			[
				[f"{topics} very interesting indeed"],
				[f"what do you like about {topics}"],
				f"I like this about {topics}|Many things|",
				[f"Very interesting"]
			]

	print("Note: If the program asks you to carry on the conversation, type in 'yes'; if you want to switch subjects")
	print("type in 'switch subject', and if you want to stop conversation type in 'no'")
	expected = 1 # The expected amount of conversation
	topics = ["Business", "Sports", "Life", "Economy", "The Pandemic"]
	sports = input("") # Experimenting with user inputs for conversation purposes
	if userResponse == "Business":
		Business = input("")
		[
			[f"What aspect of business are you interested in?"],
			f"{Business}|Maybe {Business}|Any business in general",
			[f"Hmmmmm, {Business} is very interesting indeed. I am not an expert at business, but I can carry a conversation :-)"], convo()
		],
		# The variables dedicated to carrying on conversation
		[
			[f"Do you wish to carry the conversation"], convo(),
			
		]
		for userResponse in topic:
			[f"Do you wish to continue our conversation?"]
			if userResponse == "no" or userResponse ==  "No":
				[f"Any other subject to talk about?"]
			elif userResponse == "yes" or userResponses == "Yes":
				pass
		return Business
	elif userResponse == "Sports":
		sports = input("")
		[
			[f"What sports are you into?"],
			f"I am into {sports}|My favorite sports is {sports}|I like any sports, especially {sports}",
			[f"{sports} is a very fun sport, do you play or watch {sports}?"],
			f"Yeah, of course I do!|No, just play"
		]
		#return AIresponse and userResponse
# The main AI code and program will implemented here
name = input("")
conversation = [
	[
		f"Hey|Hi|Hello|Yo|Wassup",
		[f"Hey there! what waas the name given to you?"], name,
		f"My name is {name}|The name givent to me is {name}|{name}"
	],
	[
		f"What is your functionality|How do you work?|what is your purpose?",
		[f"I am your Artificial Intellegence friend"],
		[f"Your personal assistant, like my friends Siri and Alexa"]
	],
	[
		f"What would you like to talk about?|Up for a discussion?|Let's talk",
		# Giving information on the AI subject capability
		[print("What would you like to talk about? Business, Sports, Life, Economy, The Pandemic")],
		["Those subjects will be updated in the future"], ConversationSubject()
	],
	[
		f"Code pending...",
		[f"If you wrote 'Code pending...' you found my inner thoght :-p"]
	],
]
def questions():
	# When going to deep on conversation the AI will ask a random question
	questions = ["When is the last time you experienced nostalgia?", "What's the scariest dream you've ever had?", "What's the weirdest thought you've ever had?", "What's the first thing that comes to mind when you hear the word “fidget”?", "What made-up word would you incorporate into the English language if you could?"]
	if conversation == len(conversation).strip():
		outcome = random.randint(questions)
		[
			# Type in the code
		]
		# When the statement; or, basically this whole statements does not apply
		for conversation[questions] in not questions:
			questions -= 1
			return questions
		# When the statement applies
		for conversation[questions] in questions:
			pass
# The life of Mike will depend on these two lines of code
chat = Chat(conversation, reflections)
chat.converse()
# THe start of the program
if __name__ == "__main__":
	mikeTheChatbot()