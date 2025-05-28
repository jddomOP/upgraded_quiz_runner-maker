#welcome, I'm still in the process of coding in OOP structure and this will serve as my practice also

class quiz_questions:
    def __init__(self, question, difficulty, choices, correct):
        self.questions = question
        self.difficulty = difficulty
        self.choices = choices
        self.correct = correct

    def __str__(self):
        formatted = f"Q: {self.questions}\n"
        formatted += f"Difficulty: {self.difficulty}\n"
        for key in ["a, b, c, d"]:
            formatted += f"{key}. {self.choices[key]}\n"
        formatted += f"Answer: {self.correct}\n"
        return formatted
    

