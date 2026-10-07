import pandas as pd

# Initial dataset
lessons_dict = {
    "Python Basics": 10,
    "Variables": 10,
    "Data Types": 9,
    "Conditionals": 8,
    "Loops": 9
}

MAX_SCORE_PER_ITEM = 10

def menu():
    """Displays the interactive menu and returns a valid option (1-3)."""
    while True:
        print('\n-------- MENU ----------')
        print('1. Add Topics Learned')
        print('2. View Topics Learned')
        print('3. Exit')
        
        try:
            options = int(input('\nChoose an option (1-3): > '))
            if options in [1, 2, 3]:
                return options
            else:
                print('\nError: Enter a number from 1 to 3 only.')
        except ValueError:
            print('\nError: Please enter a valid whole number (no letters).')

# --- MAIN PROGRAM START ---
print('\nTell us your name')
name = input('>')

while True:
    choice = menu()
    
    # OPTION 1: ADD TOPICS
    if choice == 1:
        print('\n------- Add a new Topic --------')
        new_topic = input('Enter topic name: ').strip()

        if not new_topic:
            print('\nWarning: Topic name cannot be empty.')
            continue

        try:
            score_input = int(input(f'Enter topic score for {new_topic} (0-{MAX_SCORE_PER_ITEM}): '))
            if 0 <= score_input <= MAX_SCORE_PER_ITEM:
                lessons_dict[new_topic] = score_input
                print(f"Successfully added '{new_topic}' with a score of {score_input}!")
            else:
                print(f"Error: Score must be between 0 and {MAX_SCORE_PER_ITEM}.")
        except ValueError:
            print("Error: Invalid input. Score must be a whole number.")

    # OPTION 2: VIEW REPORT
    elif choice == 2:
        if not lessons_dict:
            print("\nYour learning log is currently empty.")
            continue

        print(f'\nThanks {name}. Here is your updated learning log.')
        
        # Convert dictionary to DataFrame
        df = pd.DataFrame(list(lessons_dict.items()), columns=['Topic', 'Score'])
        
        # Add Percentage column
        df['Percentage'] = (df['Score'] / MAX_SCORE_PER_ITEM * 100).astype(int).astype(str) + '%'
        print("\n" + df.to_string(index=False))

        # Metrics calculation using Pandas
        total_score = df['Score'].sum()
        average_score = df['Score'].mean()
        highest_score = df['Score'].max()
        highest_topic = df.loc[df['Score'].idxmax(), 'Topic'] 
        
        total_possible_score = len(df) * MAX_SCORE_PER_ITEM
        total_percentage = (total_score / total_possible_score) * 100

        # Conditional results block
        if total_percentage >= 80:
            status = "Ready for the next step"
        elif total_percentage >= 50:
            status = "Keep practicing"
        else:
            status = "Review lessons 1-6"

        # Output performance metrics
        print('\n========= Performance Matrix ===========')
        print(f'Total Score:        {total_score} / {total_possible_score}')
        print(f'Highest Score:      {highest_score} ({highest_topic})')
        print(f'Average Score:      {average_score:.2f} / {MAX_SCORE_PER_ITEM}')
        print(f'Overall Percentage: {total_percentage:.2f}%')
        print(f'Your Status:        {status}')
        print('========================================')

    # OPTION 3: EXIT
    elif choice == 3:
        print(f'\nGoodbye {name}! Keep up the great learning.')
        break
