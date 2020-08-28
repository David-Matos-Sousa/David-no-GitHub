from random import randint

print('Lets play JOKENPO!!!')
print('Write [1] for rock')
print('Write [2] for paper')
print('Write [3] for scissors')
options = ('0', 'rock', 'paper', 'scissor')
player = int(input('What is your move?'))
computer = randint(1, 3)

print('You had selected {} and the computer had chosen {}'.format(options[player], options[computer]))

if computer == 3 and player == 1 or computer == 2 and player == 3 or computer == 1 and player == 2:
    print('Congrats you have win this match!!!')
elif computer == player:
    print('This is a tie in the game, try again :)')

else:
    print('Game over try again')
