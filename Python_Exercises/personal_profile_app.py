import pandas as pd

users = []

user1 = {
	'name': 'John Doe',
	'age': 21,
	'height': 159.4,
	'weight': 65.62,
	'is_graduate': True,
	'favorite_books': ', '.join(['Shadowhunters', 'Percy Jackson', 'Troy'])
	}
	
user2 = {
	'name': 'Mary Grace',
	'age': 19,
	'height': 142.5,
	'weight': 54.35,
	'is_graduate': True,
	'favorite_books': ', '.join(['Harry Potter', 'Narnia', 'Illiad'])
	}
users.append(user1)
users.append(user2)

for user in users:
	print(f'Hello my name is {user['name']}, {user['age']} years old. I am {user['height']}cm tall and weigh {user['weight']}kg.')
	print(f'My favorite books are {user['favorite_books']}.\n')
	
df = pd.DataFrame(users)
print(df)
