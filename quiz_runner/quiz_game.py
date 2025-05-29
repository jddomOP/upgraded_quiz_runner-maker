import random
import pyfiglet
from inputimeout import inputimeout, TimeoutOccurred
from colorama import init, Fore, Style
from quiz_storage import QuizStorage

init(autoreset=True)

class QuizGame:
    def __init__(self, storage, time_limit = 15):
        self.storage = storage
        self.time_limit = time_limit
        self.difficulty = None
        self.questions = []

    def choose_difficulty(self):
        difficulty_map = {'1': 'Elementary', '2': 'High School', '3': 'General'}

        while True:
            print(Fore.CYAN + "🔍 Select difficulty:")
            print("1. Elementary")
            print("2. High School")
            print("3. General")
            choice = input(Fore.CYAN + "Enter 1/2/3: ")

            if choice not in difficulty_map:
                print(Fore.RED + "❌ Invalid choice. Please choose between 1, 2, 3")
                continue

            self.difficulty = difficulty_map[choice]
            loaded = self.storage.load_questions_by_difficulty(self.difficulty)

            if loaded is None:
                print(Fore.RED + "QUIZ FILE NOT FOUND :(")
                return False

            if loaded:
                self.questions = loaded
                return True
            else:
                print(Fore.RED + f"No Questions found for '{self.difficulty}'. Please pick another difficulty.\n")

    def ask_questions(self):
        score = 0
        random.shuffle(self.questions)

        for i, q in enumerate(self.questions, 1):
            print(Fore.LIGHTYELLOW_EX + f"\n Questions {i}: {q['question']}")
            print(f"a.) {q['a']}")
            print(f"b.) {q['b']}")
            print(f"c.) {q['c']}")
            print(f"d.) {q['d']}")
            print(Fore.BLUE + f"⏳ You have {self.time_limit} seconds to answer!!")

            try:
                answer = inputimeout(prompt=Fore.CYAN + "Your answer (a/b/c/d): ", timeout=self.time_limit).lower()
            except TimeoutOccurred:
                answer = None
                print(Fore.RED + "⌛ Your time is up!")

            if answer in ['a', 'b', 'c', 'd'] and answer == q['correct']:
                print(Fore.GREEN + "You are Correct!!")
                score += 1
            elif answer:
                print(Fore.RED + f"❌ Wrong! The correct answer was '{q['correct']}: {q[q['correct']]}'")
            else:
                print(Fore.RED + f"❌ No answer?!?! The correct answer was '{q['correct']}: {q[q['correct']]}'")

        print(Fore.LIGHTGREEN_EX + f"\n Quiz Finished!! Your Score: {score}/{len(self.questions)}")

    def start(self):
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + pyfiglet.figlet_format("Welcome to my Quiz!!", font="slant")
              + Style.RESET_ALL)

        if self.choose_difficulty():
            self.ask_questions()


