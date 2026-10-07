# import random module
import random as rd, sys

print('ROCK, PAPER, SCISSORS')
# Variables to keep the score
wins = 0
losses = 0
ties = 0

# The main game loop
while True: 
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    # The player input loop
    while True:
        print('\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('>')

        # Player move Conditions
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break the player input loop
        print('Type one of r, p, s, or q.')

    # Display what the player chose
    if player_move == 'r':
        print('ROCK vs...')
    elif player_move == 'p':
        print('PAPER vs...')
    elif player_move == 's':
            print('SCISSORS vs...')

    # Display what the computer chose
    move_num = rd.randint(1, 3)
    if move_num == 1:
        computer_move = 'r'
        print('ROCK')
    if move_num == 2:
        computer_move = 'p'
        print('PAPER')
    if move_num == 3: 
        computer_move = 's'
        print('SCISSORS')

    # Display and record score (win, lose, tie)
    if player_move == computer_move:
        print('It is a Tie!')
        ties =+ ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins =+ wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins =+ wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins =+ wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1