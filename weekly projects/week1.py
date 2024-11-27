import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    print("Choose one: rock, paper, scissors")
    player_choice = input("Your choice: ").lower()

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please pick rock, paper, or scissors.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
