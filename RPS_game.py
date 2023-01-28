#RPS Game!
import random
def play():
    user = input("Rock, Paper or Scissors? ").lower()

#Computer choices
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options).lower()

#Functions to play game
    print(computer_choice)
    if user == computer_choice:
        print("It's a tie!")
    elif user == "Rock" and computer_choice == "Scissors":
        print("You Win!")
    elif user == "Paper" and computer_choice == "Rock":
        print("You Win!")
    elif user == "Scissors" and computer_choice == "Paper":
        print("You Win!")
    else: 
        print("You Lose!")

def main():
    play()
    while True:
        test = input("You want to play again? Y/N\n").upper() 
        if test == "Y":
            play()
        else:
            break
#Run the game
main()



 