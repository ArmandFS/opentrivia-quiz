#import requests library for API connection
import requests


#set parametes for API Request
parameters = {
    "amount": 20,
    "type" : "boolean"
}
response = requests.get("https://opentdb.com/api.php?amount=20&category=9&difficulty=medium&type=boolean", params = parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


#--------------------------------------------------------------------------Class Part-----------------------------------------------------------------------#

#we make the question class for the text(question that's being asked) and the answer
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        
        
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
            
#-----------------------------------------------------------USER INTERFACE-------------------------------------------------------------------------------#
from tkinter import *
THEME_COLOR = "#375362"
class QuizInterface:
    #as always, initiate the class with def init
    #as we are adding a method from the quizbrain class, we need to call it as a class data type
    def __init__(self, quiz_brain: QuizBrain):
        #Tkinter GUI Settings and Configs
        self.quiz = quiz_brain
        #we apply the self function to every variable that will be used in the class
        #window with theme color
        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        
        #score label with white color
        self.score_label = Label(text = "Score: 0", fg = "white", bg =THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas (width = 500, height = 350, bg = "white")
        
        #implement question text
        self.question_text = self.canvas.create_text(
            250,
            125,
            width = 480,
            text = "Sample Question Text",
            fill ="black",            
            font = ("Arial", 20, "bold")
        )
        #implement canvas and buttons with true and false images
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)
        
        true_image = PhotoImage(file ="true.png")
        self.true_button = Button(image = true_image, highlightthickness=0, command = self.true_pressed)
        self.true_button.grid(row = 2, column = 1)
        
        false_image = PhotoImage(file = "false.png")   
        self.false_button = Button(image = false_image, highlightthickness=0, command = self.false_pressed)
        self.false_button.grid(row = 2, column = 0)
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        #if the quiz still has questions, then continue on
        if self.quiz.still_has_questions():
            #implement the quiz score updater here as a score label configuration
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            #apply q text into the tkinter canvas and configure it as an item
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the Quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)   
      
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    
    
#---------------------------------------------------------------------Quiz----------------------------------------------------------------------------------#

#now we make a question bank (make it into a list) and make it a for loop so that it can loop
#through all the data
question_bank = []
#for loop to get all the objects and variables
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#apply the quizbrain object to the quizdata/bank
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)






