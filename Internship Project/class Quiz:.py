class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")

    def check_answer(self, question, answer):
        correct_answer = question['answer']
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    def start_quiz(self):
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Enter your answer (1, 2, 3, etc.): ")
            while not user_answer.isdigit() or int(user_answer) not in range(1, len(question['options']) + 1):
                user_answer = input("Invalid input. Please enter a valid option number: ")
            self.check_answer(question, question['options'][int(user_answer) - 1])
            print()  # Add an empty line for better readability
        print("Quiz completed!")
        print("Your final score is:", self.score)


questions = [
    {
        'question': "Which of the following is a Python data type?",
        'options': ["int", "string", "both a and b"],
        'answer': "both a and b"
    },
    {
        'question': "What is the output of 'print(2 ** 3)' in Python?",
        'options': ["8", "6", "16"],
        'answer': "8"
    },
    {
        'question': "Which keyword is used to define a function in Python?",
        'options': ["func", "define", "def"],
        'answer': "def"
    }
]


quiz = Quiz(questions)
quiz.start_quiz()
