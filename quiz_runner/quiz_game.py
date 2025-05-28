import random
from inputtimeout import inputimeout, TimeoutOccured
from colorama import Fore

class Quizgame:
    def __init__(self, difficulty, questions, time_limit = 15):
        self.difficulty = difficulty
        self.questions = questions
        self.time_limit = time_limit
        