import random

while True:
    computer_choice = random.choice(["rock", "paper", "scissors"]).lower()
    
    user_input = input("Enter 'rock' (r), 'paper' (p), or 'scissors' (s): ").lower()

    # Convert short form input to full form
    if user_input == "r":
        user_input = "rock"
    elif user_input == "p":
        user_input = "paper"
    elif user_input == "s":
        user_input = "scissors"

    # Check game outcomes
    if user_input == computer_choice:
        print(f"Computer chose {computer_choice}.")
        print(f"You chose {user_input}.\n")
        print("It's a draw!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print(f"Computer chose {computer_choice}.")
        print(f"You chose {user_input}.\n")
        print("You win this round!")
    elif (user_input == "rock" and computer_choice == "paper") or \
         (user_input == "paper" and computer_choice == "scissors") or \
         (user_input == "scissors" and computer_choice == "rock"):
        print(f"Computer chose {computer_choice}.")
        print(f"You chose {user_input}.\n")
        print("You lose this round!")
    else:
        print("Invalid input. Please choose either 'rock', 'paper', or 'scissors'.")
    
    # Ask if the user wants to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "n":
        print("Thanks for playing!")
        break
