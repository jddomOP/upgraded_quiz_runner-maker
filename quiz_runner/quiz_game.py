import random
from inputtimeout import inputimeout, TimeoutOccured
from colorama import Fore

class Quizgame:
    def __init__(self, difficulty, questions, time_limit = 15):
        self.difficulty = difficulty
        self.questions = questions
        self.time_limit = time_limit

    def start(self):
        random.shuffle(self.questions)

        for i, q in enumerate(self.questions, 1):
            print(Fore.YELLOW + f"\n Question {i}: {q['question']}")
            print(f"a.) {q['a']}")
            print(f"b.) {q['b']}")
            print(f"c.) {q['c']}")
            print(f"d.) {q['d']}")
            print(Fore.BLUE + f"⏳ You have {self.time_limit} seconds to answer!!")

            try:
                answer = inputimeout(prompt=Fore.CYAN + "Your answer (a/b/c/d): ", timeout=self.time_limit).lower()
            except TimeoutOccurred:
                answer = None
                print(Fore.RED + "⌛ Time is up!")

            self.check_answer(answer, q)

            print(Fore.MAGENTA + f"\n Quiz Finished!! Your Score: {self.score}/{len(self.questions)}")

    def check_answer(self, answer, question):
        correct = question['correct']
        if answer in ['a', 'b', 'c', 'd'] and answer == correct:
            print(Fore.GREEN + "✅ Correct!!")
            self.score += 1
        elif answer:
            print(Fore.RED + f"❌ Wrong! The correct answer was '{correct} {question[correct]}'")
        else:
            print(Fore.RED + f"❌ No answer?!?! The correct answer was '{correct} {question[correct]}'")