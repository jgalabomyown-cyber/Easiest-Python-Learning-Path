# Project Challenge

## Build a Personal Learning Progress Tracker

Create a console program that tracks a student's progress across your Python learning path and prints a summary report. Use only concepts from Lessons 1-6.

### Goal
Show that you understand variables, data types, operators, type conversion, conditions, loops, and basic Python modules in one working program.

### Requirements
- Create a dictionary that stores at least 5 learning topics and scores.
- Ask the user for their name and at least 3 topic scores using `input()`.
- Convert those scores from strings to integers using `int()`.
- Use a `for` loop to calculate:
  - total score
  - average score
  - highest score
- Use an `if` / `elif` / `else` block to assign a result:
  - average 80 or higher: `Ready for the next step`
  - average 50-79: `Keep practicing`
  - average below 50: `Review lessons 1-6`
- Use at least one Boolean operator such as `and`, `or`, or `not`.
- Use `type()` to show the type of the score dictionary and the average value.
- Use f-strings or string concatenation to print the final summary.
- Validate each score is between 0 and 100 using a `while` loop.
- Use `break` or `continue` at least once.
- Use `range()` to number the learning topics or loop through them.

### Suggested topics
- Variables
- Math Operators
- Data Types
- Type Casting
- If/Else Logic
- Loops

### Example output
```text
Student: Alex
Topic scores: {'Variables': 90, 'Math': 85, 'Data Types': 78, 'Casting': 88, 'If/Else': 92, 'Loops': 94}
Total score: 527
Average score: 87.83
Highest score: 94
Result: Ready for the next step
```

### Bonus challenges
- Add a menu with options to view scores or exit with `sys.exit()`.
- Store the scores in a list as well as a dictionary.
- Add a NumPy array to square the scores.
- Use Pandas to build a small DataFrame and filter scores above 80.
- Let the user retry bad scores until they enter valid values.

### Submission
Save your file as:
`Python_Exercises/personal_learning_tracker.py`

### Challenge level
Beginner to Intermediate

### Estimated time
45-60 minutes
