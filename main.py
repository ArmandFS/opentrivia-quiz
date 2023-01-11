
from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface


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
