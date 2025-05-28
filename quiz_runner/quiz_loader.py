import os
from colorama import Fore

filename = 'quiz_questions_and_answers'

def load_questions_by_difficulty(difficulty):
    if not os.path.exists(filename):
        print(FORE.RED + "QUIZ FILE NOT FOUND...")
        return []

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()

    question_blocks = content.split("-"*40 + "\n")
    question = []

    for block in question_blocks:
        lines = block.strip().split('\n')
        if len(lines) < 7:
            continue

        question_data = {
            "question": lines[0][3:],
            "difficulty": lines[1][11:].strip().lower(),
            "a": lines[2][4:],
            "b": lines[3][4:],
            "c": lines[4][4:],
            "d": lines[5][4:],
            "correct": lines[6][8:].lower()
        }