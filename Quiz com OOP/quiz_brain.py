class QuizBrain:
    def __init__(self,  q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = ""
        while user_answer not in ["True", "False"]:
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):").capitalize()
            if user_answer not in ["True", "False"]:
                print("Digite 'True'  ou 'False'.")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Você acertou!")
            self.score += 1
        else:
            print("Você errou.")
        print(f"A resposta correta é {correct_answer}.")
        print(f"Sua pontuação atual é: {self.score}/{self.question_number}.")
        print("\n")
