#here is the quiz app where we can make questions for the quiz

import pyfiglet
from quiz_storage import Quizstorage
from quiz_questions import Quizquestion

class Quizrunner:
    def __init__(self):
        self.storage = Quizstorage()

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
                self.delete_question()
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

            choices = {
                'a':input("Choice a: "),
                'b':input("Choice b: "),
                'c':input("Choice c: "),
                'd':input("Choice d: ")
            }

            correct = ""
            while correct.lower() not in ['a', 'b', 'c', 'd']:
                correct = input("Enter the correct answer (a/b/c/d): ").lower()
                if correct not in choices:
                    print("Invalid input! Please choose from a, b, c, d 😊")

            quiz_questions = Quizquestion(question, difficulty, choices, correct)
            self.storage.save_question(quiz_questions)
            print("Question is saved!!\n")

    def view_questions(self):
        questions = self.storage.load_all_questions()
        if not questions:
            print("No questions saved yet.")
            return

        print("\n=== SAVED QUIZ QUESTIONS ===")
        for q in questions:
            print(q + "\n" + "-" * 40)

    def delete_question(self):
        questions = self.storage.load_all_questions()
        if not questions:
            print("No questions to delete.")
            return

        print("\n=== Questions ===")
        for i, q in enumerate(questions, start=1):
            print(f"{i}. {q.splitlines()[0]}")

        user_input = input("Enter the number of the question to delete (or 'cancel'): ")
        if user_input.lower() == 'cancel':
            print("Deletion cancelled.")
            return

        try:
            index = int(user_input) - 1
            if self.storage.delete_question(index):
                print("Question deleted successfully.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Must be a number or 'cancel'.")




