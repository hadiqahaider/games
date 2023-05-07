import random

def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

user = input("'r','p','s'\n")
computer = random.choice(['r','p','s'])
print(f"computer chose {computer}")
    
if user == computer:
    print( 'tie')
    

if is_winner(user, computer):
    print('you won')

elif is_winner(computer, user):
    print( 'you lost')

def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
