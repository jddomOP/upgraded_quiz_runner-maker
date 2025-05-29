#Here is where the question will be read

import os

class QuizStorage:
    def __init__(self), filename = 'quiz_questions_and_answers':
    self.filename = filename

    def load_questions_by_difficulty(self, difficulty):
        if not os.path.exists(self.filename):
            return None
