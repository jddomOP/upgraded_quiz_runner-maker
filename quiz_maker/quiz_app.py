#here is the quiz app where we can make questions for the quiz

import pyfiglet
from quiz_storage import quiz_storage
from quiz_questions import quiz_questions

class quiz_runner:
    def __init__(self):
        self.storage = quiz_storage()

    def display_title(self):
        print(pyfiglet.figlet_format("Welcome to the Quiz Maker!", font = 'slant'))

    def main_menu(self):
        while True:
            self.display_title()
            print("Main Menu")
            print("1. Create a Quiz")
            print("2. View Questions")
            print("3. Delete questions")
            print("4. Exit")
            choice = input("Choose an option! (1,2,3,4): ")

            


