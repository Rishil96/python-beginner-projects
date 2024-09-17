class Question:
    """
    Models the Question class where each question object contains the question and its answer
    """
    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer

    # Print the object in formatted way to not display memory location when printed
    def __repr__(self):
        return f"({self.text} => {self.answer})"
