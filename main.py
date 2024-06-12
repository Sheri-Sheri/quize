from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
question_bank =[]
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question=Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"you have complete the quize")
print(f"you'r final score is {quiz.score}/{quiz.question_number}")

