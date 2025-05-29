#Here is where the question will be read

import os

class QuizStorage:
    def __init__(self), filename = 'quiz_questions_and_answers':
    self.filename = filename

    def load_questions_by_difficulty(self, difficulty):
        if not os.path.exists(self.filename):
            return None

        with open(self.filename, 'r', encoding = 'utf-8') as file:
            content = file.read().strip()

        question_blocks = content.split('-'*40 + '\n')
        questions = []

        for block in question_blocks:
            lines = block.strip().split('\n')
            if len(lines) < 7:
                continue
