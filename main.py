from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    q_text = data["text"]
    q_answer = data["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.more_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Total Score: {quiz.score}/{quiz.question_number}")



