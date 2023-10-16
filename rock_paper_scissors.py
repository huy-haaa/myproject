import random
def game():
    user = input("r = rock , p = paper, s = scissors\n")
    computer = random.choice(['r','p','s'])
    print(f"computer is pick {computer}")
    #r > s  , s > p , p > r
    if user == computer:
        return "draw, play again"
    if user_win(user,computer):
        return 'You won !!'
    return 'you lost'
#r > s  , s > p , p > r
def user_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
print(game())




