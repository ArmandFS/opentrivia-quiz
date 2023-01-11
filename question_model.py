#we make the question class for the text(question that's being asked) and the answer
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        