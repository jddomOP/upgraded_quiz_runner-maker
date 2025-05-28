import os
from colorama import Fore

filename = 'quiz_questions_and_answers'

def load_questions_by_difficulty(difficulty):
    if not os.path.exists(filename):
        print(FORE.RED + "QUIZ FILE NOT FOUND...")
        return []