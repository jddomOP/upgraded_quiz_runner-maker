from quiz_loader import load_questions_by_difficulty
from colorama import Fore

def choose_difficulty():
    difficulty_map = {'1': 'Elementary', '2': "High School", '3': 'General'}

    while True:
        print(Fore.CYAN + "🔍 Select difficulty:")
        print("1. Elementary")
        print("2. High School")
        print("3. General")
        choice = input(Fore.CYAN + "Enter 1/2/3: ")