import random
import pyfiglet
from inputimeout import inputimeout, TimeoutOccurred
from colorama import init, Fore, Style
from quiz_storage import QuizStorage

init(autoreset=True)

class QuizRunner:
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
                return  False

            if loaded:
                self.questions = loaded
                return True
            else:
                print(Fore.RED + f"No Questions found for '{self.difficulty}. Please pick another difficulty.\n")

        def ask_questions(self):
            
