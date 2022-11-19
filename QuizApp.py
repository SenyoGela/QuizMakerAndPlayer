import pprint

all_quizzes = {"SENSORY ORGAN":{"Sense of taste":"tounge", "Sense of smell":"nose", "Sense of hearing":"ears", "Sense of sight":"eyes", "Sense of touch":"skin"}}

while True:
	#display menu
	print("")
	print("********** MENU **********")
	print("(1) Create Quiz")
	print("(2) Answer Quiz")
	print("(3) View All Quiz")
	print("(4) Delete Quiz")
	print("(5) Exit")
	print("**************************")
	print("")
	
	#ask user what to do
	menu_input = int(input("What do you want to do? "))
	
	#if input = 1
	print("")
	if menu_input == 1:
		num_questions = int(input("How many questions do you want your quiz to have? "))
		quiz_title = str(input("What is the title of your quiz? ")).upper()
		print("")
		new_quiz = {}
		for x in range(num_questions):
			question = str(input("Enter question: "))
			answer = str(input("Enter answer : ")).lower()
			ques_ans = {question:answer}
			new_quiz.update(ques_ans)
			add_quiz = {quiz_title:new_quiz}
			all_quizzes.update(add_quiz)
			print("")
	
	#if input = 2
	print("")
	if menu_input == 2:
		score = 0
		print("========== Quizzes ==========")
		pprint.pprint(all_quizzes.keys())
		print("")
		answer_what_quiz = str(input("Enter the title of the quiz you want to answer: ")).upper()
		if answer_what_quiz in all_quizzes.keys():
			for key in all_quizzes[answer_what_quiz]:
				print("Question:", key)
				user_answer = str(input("Answer: ")).lower()
				my_quiz = all_quizzes[answer_what_quiz]
				if user_answer == my_quiz.get(key):
					score += 1
					print("Correct!")
				else:
					print("Wrong!")
		print("")						
		print("Score:", score, "out of", len(my_quiz))
						
	#if input = 3
	if menu_input == 3:
		print("")
		print("========== Quizzes ==========")	
		pprint.pprint(all_quizzes.keys())
		print("")					
	
	#if input = 4
	if menu_input == 4:
		print("")
		print("========== Quizzes ==========")
		pprint.pprint(all_quizzes.keys())
		print("")
		delete_quiz = str(input("Enter the title of the quiz you want to delete: ")).upper()
		if delete_quiz in all_quizzes.keys():
			del all_quizzes[delete_quiz]
			print("The quiz entitled", delete_quiz, "has been deleted.")
			print("")
			print("Here are the new list of quizzes")
			pprint.pprint(all_quizzes.keys())
			print("")
		else:
			print("Quiz not found!")
			print("")
	
	#if input = 5
	if menu_input == 5:
			exit = str(input("Are you sure you want to exit(y/n)? ")).lower()
			if exit == "y":
				break
			

