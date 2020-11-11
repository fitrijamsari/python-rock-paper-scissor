import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor\n" )
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie'

    # r > s, p > r , s > p

    if is_win(user, computer):
        return 'You won!'

    return 'You lost'

def is_win(player, opponent):
    #return true if player win
    # r > s, p > r , s > p
    if (player == 'r', opponent== 's') or (player == 'p', opponent== 'r') or (player == 's', opponent== 'p'):
        return True

print(play())
