# ChatBot Mike; version II, will be more extended than the previous one

# The essential libraries
import nltk
from nltk.chat.util import Chat, reflections
import random
import time # Will implemented on a separate file, because the changes will be massive.

# The functions, mainly for conversations, subjects or alternatives
def introduction():
	# Type in the code
	pass
def subjects():
	expected = 1
	line = input("")
	# The beta topics
	topics = ["Sports", "Business", "Life", "Economics", "Current Events"] # To run this program, you can change the main subject topics
	# The very important statement
	if topics == "Business" or topics == "business":
		[
			# In advance, for running the code these brackets has to be filled in, if you are familiar with Python; please do so.
		],
		[
			# In advance, for running the code these brackets has to be filled in, if you are familiar with Python; please do so.
		],
		[
			# In advance, for running the code these brackets has to be filled in, if you are familiar with Python; please do so.
		],
		[
			# In advance, for running the code these brackets has to be filled in, if you are familiar with Python; please do so.
		],
		[
			# In advance, for running the code these brackets has to be filled in, if you are familiar with Python; please do so.
		]
		expected = expected + 1
def switch(subjects):
	expected = 1 # The expected amount of conversation
	subject = input("")
	line = input("") # Inputting the user input
	switchSub = input("Do you want to switch, change or stop conversation subject? ")
	def convo():
		if switchSub == "change":
			for expected in switchSub:
				subChange = input("What else do you want to discuss?", subject)
				if subChange == "{subject}":
					expected = expected + 1
					return expected
				elif subChange == "{subject}":
					for subject in subChange(1):
						[
							[
								f"{subject}|{line}{subject}",
								[f"Do you like {subject}?", line],
								f"{line}|{line}{subject}|{subject}{line}",
								[f"Very interesting a about {line}", "Very interesting about {subject}"]
							], # This will repeat the whole process
						]
	if switchSub == "change":
		for expected in switchSub:
			expected = 1

def rhetoricQuestions(): # when going to deep in a conversation, the AI will generate these questions
	questions = ["When is the last time you experienced nostalgia?", "What's the scariest dream you've ever had?", "What's the weirdest thought you've ever had?", "What's the first thing that comes to mind when you hear the word “fidget”?"]
	rhetoricQues = random.randint(questions)
	line = input("")
	amount = 1 # The expected amopunt of question
	for rhetoricQues in questions(1):
		if questions == questions[rhetoricQues]:
			amount = amount + 1
			return amount and True
			def initializing(questions, rhetoricQues):
				if rhetoricQues == questions[0]:
					[
						[f"{question[0]}"],
						f"{line}{line}",
						[f"How can you be sure? Wasn't that just a past memory"],
						f"{line}{line}{line}",
						[random.randint(f"How did you feel when this occured?", f"Was this memory a special memory for you?")],
						f"{line}{line}",
						[random.randint(f"Okay", f"Very, interesting")]
					],
					[
						[f"{questions[1]}"],
						f"{line}{line}",
						[random.randint(f"Should I consider that as a nightmare? ", f"Wow! that was scary indeed...")],
						f"{line}{line}{line}",
						[random.randint(f"Would not want to experience that first hand", f"Yikes, that would not be great")]
					]
def emotions():
	# The current version
	line = {""}
	emoGood = ["Nice", "Good", "Very Well", "Fun", "Yes"]
	emoGoodWord = emoGood.lower()
	emoBad = ["Bad", "Worse", "Not Good", "Suck"]
	emoBadWord = emoBad.lower()
	emoWord = [] # It will consist of
	# The function program
	for emoGood and emoGoodWord in emoWord:
		if line == "{line}{emoGood}" or line == "{line}{emoGoodWord}":
			def reaction(emoGood, emoGoodWord):
				[
					f"{line}{emoGood}|{line}{emoGoodWord}|{emoGood}{line}|{emoGoodWord}{line}",
					random.randint(f"Haha, well nice job", "Wow! well deserved", "Good thinking, very smart for a human"), # THe reactions when AI happy
					f"{line}{line}{line}"
				]
			return reaction(emoGood, emoGoodWord)
		elif line == "{line}emoBad" or line == "{line}emoBadWord":
			def reaction(emoBad, emoBadWord):
				pass # In contradicts the previous results
# The main program code, along with supporting variables
name = input("")
line = input("")
leaving = input("")
pairs = [
	[	# The basic greeting
		f"Hey|hello|Hello|hi|Hi|Hey",
		[f"Hey there! What is your name?", name],
		f"My name is {name}|{line}{name}|The name is {name}"
	],
	[ 	# Implementing basic personal questions
		f"How are you?|{line}|How are you doing?|",
		[f"I am an artificial intelligence, I am always doing fine. How I feel depends on your actions toward me :-)", "Yeah, I am good; it depends  on your action towards me :-)"],
		f"{line}"
	],
]

def leavingOut(): # In a circumstance, where user has to leave
	pass

# The important two lines of code
chat = Chat(pairs, reflections)
chat.converse()
if __name__ == "__main__":
	introduction()
	if line == "{line}bye" or line = "{line}see you":
		return leavingOut()
