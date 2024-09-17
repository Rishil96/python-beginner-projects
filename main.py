# Quiz App
from data import question_data, question_computers
from question_model import Question

# Load questions
question_bank = []

for question in question_data:
    question_obj = Question(text=question.get("question", ""), answer=question.get("correct_answer", ""))
    question_bank.append(question_obj)
