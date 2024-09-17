class Question:
    """
    Models the Question class where each question object contains the question and its answer
    """
    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer
