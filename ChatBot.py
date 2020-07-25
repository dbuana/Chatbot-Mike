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
