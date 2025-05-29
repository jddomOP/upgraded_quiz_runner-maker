from quiz_storage import QuizStorage
from quiz_game import QuizGame

if __name__ == "__main__":
    storage = QuizStorage()
    quiz = QuizGame(storage)
    quiz.start()