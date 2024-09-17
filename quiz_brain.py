from random import shuffle
from question_model import Question


class QuizBrain:

    def __init__(self, question_list: list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        shuffle(self.question_list)

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").title()
        self.check_answer(answer=answer, question=current_question)

    def check_answer(self, answer: str, question: Question):
        """
        Receives the user answer and the question as input and checks if the user answered correctly
        """
        if answer == question.answer:
            self.score += 1
            print("You got that right!")
        else:
            print("That was incorrect!")

        print(f"The correct answer is {question.answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")

    def still_has_questions(self) -> bool:
        """
        Returns a bool value to tell if the quiz has ended or not
        """
        return self.question_number < len(self.question_list)
