#User Interface using Tkinter

from tkinter import *
from quiz_brain import QuizBrain


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