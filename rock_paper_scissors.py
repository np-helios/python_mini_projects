import random

def RPS():
    user_input=input(f"what's your choice? 'r' for rock ,'p' for paper and 's' for scissors")
    computer_input=random.choice(['r','p','s'])
    
    if user_input == computer_input:
        print("Its a tie!!")
        
    elif (user_input=='r'and computer_input=='s') or (user_input=='p' and computer_input=='r') or (user_input=='s' and computer_input=='p'):
        print("you are the winner!!")
    else:
        print("you lose the game.")
        
    print("computer's choice was :" , computer_input)
        
RPS()
        
