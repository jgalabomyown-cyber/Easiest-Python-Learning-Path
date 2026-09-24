# Python Learning Path 1-6 Quiz
# Covers: variables, data types, string operations, operators, advanced data types,
# and type casting.

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
        "question": "What does 'Alice' + 'Bob' produce?",
        "options": [
            "a) Alice Bob",
            "b) AliceBob",
            "c) Alice + Bob",
            "d) Error"
        ],
        "answer": "b"
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
        "question": "Which operator is used for exponentiation in Python?",
        "options": [
            "a) ^",
            "b) **",
            "c) //",
            "d) %"
        ],
        "answer": "b"
    },
    {
        "question": "Which of these is a list?",
        "options": [
            "a) (1, 2, 3)",
            "b) [1, 2, 3]",
            "c) {1, 2, 3}",
            "d) {'a': 1, 'b': 2}"
        ],
        "answer": "b"
    },
    {
        "question": "Which data type stores values as key-value pairs?",
        "options": [
            "a) List",
            "b) Set",
            "c) Dictionary",
            "d) Tuple"
        ],
        "answer": "c"
    },
    {
        "question": "What is the main difference between a list and a tuple?",
        "options": [
            "a) A list is immutable and a tuple is mutable",
            "b) A list is ordered and mutable, while a tuple is ordered and immutable",
            "c) A list stores key-value pairs",
            "d) A tuple cannot store numbers"
        ],
        "answer": "b"
    },
    {
        "question": "Which value represents the absence of a value in Python?",
        "options": [
            "a) empty string",
            "b) 0",
            "c) None",
            "d) False"
        ],
        "answer": "c"
    },
    {
        "question": "What does type(age) return if age = 12?",
        "options": [
            "a) <class 'float'>",
            "b) <class 'str'>",
            "c) <class 'int'>",
            "d) <class 'bool'>"
        ],
        "answer": "c"
    },
    {
        "question": "Which is an example of explicit type conversion?",
        "options": [
            "a) a = 7; b = 2.5; c = a + b",
            "b) n = float(5)",
            "c) x = 10",
            "d) name = 'John'"
        ],
        "answer": "b"
    },
    {
        "question": "What is the result of int(5.9)?",
        "options": [
            "a) 5.9",
            "b) 6",
            "c) 5",
            "d) Error"
        ],
        "answer": "c"
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
