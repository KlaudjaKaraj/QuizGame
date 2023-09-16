from QuizGame.data import question_data
from QuizGame.question import Question
from QuizGame.quiz_logic import QuizLogic


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
#print(question_bank)


quiz = QuizLogic(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz!")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")