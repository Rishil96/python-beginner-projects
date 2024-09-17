# Quiz App
from data import question_data, question_computers
from question_model import Question
from quiz_brain import QuizBrain
from art import logo


def play_quiz():
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

    print(logo)

    # Start quiz and run till we have questions left
    while quiz.still_has_questions():
        quiz.next_question()

    # Print final score
    print(f"Your final score is {quiz.score}/{quiz.question_number}!")

    restart_quiz = input("\nWould you like to take the quiz again? Type 'y' or 'n': ").lower()
    if restart_quiz == 'y':
        play_quiz()
    else:
        print("Thanks for quizzing!")


if __name__ == "__main__":
    play_quiz()
