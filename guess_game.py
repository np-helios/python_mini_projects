import random

def guess(x):
    computer_guess = random.randint(1,x)
    user_guess=0
    while user_guess != computer_guess:
        user_guess = int(input(f"guess a random number between 1 and {x}"))
        if user_guess > computer_guess:
            print(f"that's a wrong guess! , please choose a lower number")
        elif user_guess < computer_guess:
            print(f"that's a wrong guess! , please choose a higher number")
        
    print(f"Wohoo! you guessed the right number , its {x}")
            
guess(16)