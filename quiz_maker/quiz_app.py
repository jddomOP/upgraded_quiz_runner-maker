#here is the quiz app where we can make questions for the quiz

import pyfiglet
from quiz_storage import quiz_storage
from quiz_questions import quiz_questions

class quiz_runner:
    def __init__(self):
        self.storage = quiz_storage()

    def display_title(self):
        print(pyfiglet.figlet_format("Welcome to the Quiz Maker!", font = 'slant'))



