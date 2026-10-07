import pandas as pd
lessons_dict = {
	"Python Basics": 10,
	"Variables": 10,
	"Data Types": 9,
	"Conditionals": 8,
	"Loops": 9
}

MAX_SCORE_PER_ITEM = 10

print('\nTell us your name')
name = input('>')

while True:

	print('\n------- Add a new Topic --------')

	new_topic = input('\nEnter topic name: ').strip()

	if new_topic == "":
		print('\nWarning: Topic name cannot be empty')
		continue

	new_topic_score = int(input(f'Enter topic score for {new_topic}: '))

	lessons_dict[new_topic] = new_topic_score

	print('\nDo you want to add more topics? (yes)/(no)')
	choice = input('> ').strip().lower()

	if choice == 'no' or choice == 'n':
		print('\nSaving your topics.....')
		break


print(f'\nThanks {name}. Here is your updated learning log.')

total_score = 0
highest_score = -1
highest_topic = ""

for topic, score in lessons_dict.items():
	total_score += score

	if score > highest_score:
		highest_score = score
		highest_topic = topic

average_score = total_score / len(lessons_dict)


df = pd.DataFrame(list(lessons_dict.items()), columns=['Topic', 'Score'])

df['Percentage'] = (df['Score'] / MAX_SCORE_PER_ITEM) * 100
df['Percentage'] = df['Percentage'].astype(str) + '%'

print(df.to_string(index = False))

total_possible_score = len(lessons_dict) * MAX_SCORE_PER_ITEM
total_percentage = (total_score / total_possible_score) * 100
print('\n========= Performance Matrix ===========')
print(f'Total Score: {total_score} / {total_possible_score}')
print(f'Highest Score: {highest_score} ({highest_topic})')
print(f'Average: {average_score:.2f}')
print(f'Overall Percentage: {total_percentage:.2f}%')


