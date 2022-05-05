from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

question_bank = []
for question in question_data:
    question_text = question['question']
    answer_text = question['correct_answer']
    new_question = Question(question_text,answer_text)
    question_bank.append(new_question)
    #question_bank.append(question(question['text'],question['answer']))
#print(question_bank[0].text)

quiz = Quiz_brain(question_bank)

while quiz.still_has_questions():
        quiz.next_question()

print('You are at the end of the quiz')
print(f'Your final score is {quiz.score}/{quiz.question_number}')
print(f'You performed {quiz.rating}ly')
print('\n')














   

