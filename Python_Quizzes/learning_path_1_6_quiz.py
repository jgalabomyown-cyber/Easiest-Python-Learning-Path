# Python Learning Path 1-6 Quiz
# Based directly on the lessons in this project: variables, data types,
# operators, casting, conditions, and loops.

questions = [
    {
        "question": "Which statement correctly assigns 12 to a variable named age?",
        "options": [
            "a) age == 12",
            "b) age = 12",
            "c) 12 = age",
            "d) assign age 12"
        ],
        "answer": "b"
    },
    {
        "question": "Which variable name is valid in Python?",
        "options": [
            "a) current-balance",
            "b) 2nd_name",
            "c) current_balance",
            "d) total$sum"
        ],
        "answer": "c"
    },
    {
        "question": "What does 'Alice' + 'Bob' evaluate to?",
        "options": [
            "a) Alice Bob",
            "b) AliceBob",
            "c) Alice + Bob",
            "d) Error"
        ],
        "answer": "b"
    },
    {
        "question": "Which of these is a dictionary?",
        "options": [
            "a) [1, 2, 3]",
            "b) (1, 2, 3)",
            "c) {'name': 'John', 'age': 20}",
            "d) {1, 2, 3}"
        ],
        "answer": "c"
    },
    {
        "question": "What is the result of 22 % 8?",
        "options": [
            "a) 2",
            "b) 2.75",
            "c) 6",
            "d) 8"
        ],
        "answer": "c"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": [
            "a) ^",
            "b) **",
            "c) //",
            "d) %"
        ],
        "answer": "b"
    },
    {
        "question": "What does int(5.9) return?",
        "options": [
            "a) 5.9",
            "b) 6",
            "c) 5",
            "d) Error"
        ],
        "answer": "c"
    },
    {
        "question": "Which expression is the correct comparison check?",
        "options": [
            "a) age = 12",
            "b) age == 12",
            "c) age != 12",
            "d) age === 12"
        ],
        "answer": "b"
    },
    {
        "question": "What is the result of True and False?",
        "options": [
            "a) True",
            "b) False",
            "c) None",
            "d) Error"
        ],
        "answer": "b"
    },
    {
        "question": "Which value is considered falsy in Python?",
        "options": [
            "a) 'hello'",
            "b) 1",
            "c) []",
            "d) '0'"
        ],
        "answer": "c"
    },
    {
        "question": "What does break do inside a loop?",
        "options": [
            "a) Skips one iteration",
            "b) Stops the loop immediately",
            "c) Restarts the loop",
            "d) Converts the loop to a list"
        ],
        "answer": "b"
    },
    {
        "question": "Which loop produces numbers 0, 2, 4, 6, 8?",
        "options": [
            "a) range(0, 10, 2)",
            "b) range(1, 10, 2)",
            "c) range(0, 9, 2)",
            "d) range(2, 10, 2)"
        ],
        "answer": "a"
    },
    {
        "question": "What is the purpose of continue in a loop?",
        "options": [
            "a) Ends the entire program",
            "b) Jumps to the next iteration",
            "c) Stores a value in a list",
            "d) Creates a new function"
        ],
        "answer": "b"
    },
    {
        "question": "Which statement is used to import a module?",
        "options": [
            "a) include",
            "b) require",
            "c) import",
            "d) load"
        ],
        "answer": "c"
    },
    {
        "question": "What does sys.exit() do?",
        "options": [
            "a) Pauses the program",
            "b) Exits the program early",
            "c) Prints a traceback",
            "d) Imports a new file"
        ],
        "answer": "b"
    }
]


def run_quiz():
    score = 0
    print("Python Learning Path 1-6 Quiz")
    print("Answer each question with a, b, c, or d.\n")

    for index, q in enumerate(questions, start=1):
        print(f"Question {index}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().lower()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {q['answer']}.\n")

    print(f"Your final score: {score}/{len(questions)}")


def show_answer_key():
    print("\nAnswer Key:")
    for index, q in enumerate(questions, start=1):
        print(f"{index}. {q['answer']}")


if __name__ == "__main__":
    run_quiz()
    show_answer_key()

