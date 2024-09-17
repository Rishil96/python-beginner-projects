# Quiz App
from data import question_data, question_computers
from question_model import Question
from quiz_brain import QuizBrain

# Load questions
question_bank = []

# Ask user to choose the quiz genre
quiz_genre = input("Which quiz would you like to take? Type 'general' or 'computer': ").lower()
questions_list = question_computers if quiz_genre == "computer" else question_data

for question in questions_list:
    new_question = Question(text=question.get("question", ""), answer=question.get("correct_answer", ""))
    question_bank.append(new_question)

# Initialize QuizBrain
quiz = QuizBrain(question_list=question_bank)

# Start quiz and run till we have questions left
while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score is {quiz.score}/{quiz.question_number}!")
