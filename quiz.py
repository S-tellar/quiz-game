"""
Python Quiz Game
A simple terminal quiz that asks questions, keeps score,
and shows the final result with a grade.
"""

import random

# Each question is a dictionary: the question, 4 options, and the correct option letter
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"a": "func", "b": "def", "c": "function", "d": "define"},
        "answer": "b",
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": {"a": "6", "b": "5", "c": "8", "d": "9"},
        "answer": "c",
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": {"a": "int", "b": "str", "c": "float", "d": "bool"},
        "answer": "d",
    },
    {
        "question": "Which of these is a list in Python?",
        "options": {"a": "[1, 2, 3]", "b": "(1, 2, 3)", "c": "{1, 2, 3}", "d": "<1, 2, 3>"},
        "answer": "a",
    },
    {
        "question": "What does len('Python') return?",
        "options": {"a": "5", "b": "6", "c": "7", "d": "4"},
        "answer": "b",
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {"a": "//", "b": "/*", "c": "#", "d": "--"},
        "answer": "c",
    },
    {
        "question": "Which loop is used to go through each item of a list?",
        "options": {"a": "for", "b": "if", "c": "switch", "d": "repeat"},
        "answer": "a",
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": {"a": ".pt", "b": ".pyt", "c": ".python", "d": ".py"},
        "answer": "d",
    },
]


def ask_question(number, q):
    """Show one question, take the user's answer, and return True if correct."""
    print(f"\nQuestion {number}: {q['question']}")
    for letter, text in q["options"].items():
        print(f"  {letter}) {text}")

    # Keep asking until the user types a valid option
    while True:
        choice = input("Your answer (a/b/c/d): ").strip().lower()
        if choice in q["options"]:
            break
        print("Please type only a, b, c or d.")

    if choice == q["answer"]:
        print("Correct!")
        return True

    correct_text = q["options"][q["answer"]]
    print(f"Wrong. The correct answer is {q['answer']}) {correct_text}")
    return False


def get_grade(percentage):
    """Return a grade based on the percentage scored."""
    if percentage >= 90:
        return "A+ - Excellent!"
    elif percentage >= 75:
        return "A - Great job!"
    elif percentage >= 50:
        return "B - Good effort, keep practising."
    else:
        return "C - Don't give up, try again!"


def play_quiz():
    """Run one full round of the quiz."""
    name = input("Enter your name: ").strip()
    print(f"\nWelcome, {name}! Let's start the quiz.")

    random.shuffle(questions)  # different order every time
    score = 0

    for number, q in enumerate(questions, start=1):
        if ask_question(number, q):
            score += 1

    total = len(questions)
    percentage = (score / total) * 100

    print("\n" + "=" * 35)
    print(f"Final Result for {name}")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.1f}%")
    print(f"Grade: {get_grade(percentage)}")
    print("=" * 35)


def main():
    """Let the user play again and again if they want."""
    while True:
        play_quiz()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
