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

            if choice == '1':
                self.create_quiz()
            elif choice == '2':
                self.view_questions()
            elif choice == '3':
                self.delete_questions()
            elif choice == '4':
                print("Thanks for using!!")
                break
            else:
                print("Invalid input! Please try again :)")

    def create_quiz(self):
        difficulty = input("Enter the difficulty (Elementary, High School, General): ").capitalize()
        print(f"Creating {difficulty} quiz.")

        while True:
            question = input("Enter your desired question (or type 'exit' to go back to main menu): ")
            if question.lower() == "exit":
                print("Returning to Main Menu...\n")
                break



