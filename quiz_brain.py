#apply html unescape function to get rid of html entities and correction  
import html
#quizbrain function to give the input and retrieve a question from the data
class QuizBrain:
    #starting score and question counter while also showing question list
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
    #function to measure the list if there are still any questions, if there are no more questions yet then it's false.
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
            
        
    #move on to the next question, and giving the input function for user input, also adding +1 of the question number
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        
    #check answer function, with added score +1 if else statement
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False