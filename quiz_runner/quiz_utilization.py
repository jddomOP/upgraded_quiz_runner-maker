from quiz_loader import load_questions_by_difficulty
from colorama import Fore

def choose_difficulty():
    difficulty_map = {'1': 'Elementary', '2': "High School", '3': 'General'}

    while True