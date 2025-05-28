from quiz_game import Quizgame
from quiz_utilization import choose_difficulty
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + pyfiglet.figlet_format("Welcome to my Quiz!!", font="slant"))
    difficulty, questions = choose_difficulty()
    game = Quizgame(difficulty, questions)
    game.start()

if __name__ == "__main__":
    main()