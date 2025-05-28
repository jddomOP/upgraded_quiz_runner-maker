#this will serve as a storer for questions and will serve for making .txt file

import os

class quiz_storage:
    def __init__(self, filename = 'quiz_questions_and_answers'):
        self.filename = filename

    def save_question(self, quiz_data):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(quiz_data.to_file_string())

    def load_all_questions(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r', encoding = 'utf-8') as file:
            raw = file.read
            blocks = raw.strip().split("-"*40 + "\n")
            return [block.strip() for block in blocks if block.strip()]

    def delete_question(self, index):
        questions = self.load_all_questions()
        if 0 <= index <= len(questions):
            del questions[index]
            with open (self.filename, 'w', encoding = 'utf-8') as file:
                for q in questions:
                    file.write(q + "\n" + "-"*40 + "\n")
            return True
        return False