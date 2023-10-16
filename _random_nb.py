import random
your_guess = int(input('write the number u want guess in range: '))

def guess_nb(x):
    computer_nb = random.randint(1, x )
    guess = 0
    while guess != computer_nb:
        guess = int(input("write your nb you guess : "))
        if guess > computer_nb:
            print("your nb is so high, pls guess again")
        elif guess < computer_nb:
            print("your nb is so low, pls guess again")
    print("congratulations")
guess_nb(your_guess)

#new_nb= int(input("write new number: "))
def my_nb(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randrange(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} too high(h), too low (l) or correct(c) ")
        if feedback == "l":
            low = guess +1
        elif feedback == 'h':
            high = guess -1
    print(f"congratulations, {guess} is correct ")
my_nb(your_guess)