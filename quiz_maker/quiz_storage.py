#this will serve as a storer for questions and will serve for making .txt file

import os

class quiz_storage:
    def __init__(self, filename = 'quiz_questions_and_answers'):
        self.filename = filename

    def save_question(self, quiz_data):
