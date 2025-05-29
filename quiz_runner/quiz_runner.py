import random
import pyfiglet
from inputimeout import inputimeout, TimeoutOccurred
from colorama import init, Fore, Style
from quiz_storage import QuizStorage

init(autoreset=True)

class QuizRunner:
    def __init__(self, storage, time_limit = 15):
        self.storage = storage
        self.time_limit = time_limit
        self.difficulty = None
        self.questions = []