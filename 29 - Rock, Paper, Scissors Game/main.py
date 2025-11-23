# Rock, paper, scissors game, by KYLE
import random

options = ("rock", "paper", "scissors")
play_again = "Y"

while play_again == "Y":
    opponent = random.choice(options)

    while True:
        choice = input("Rock, paper, or scissors?: ").lower()
        if (choice != "rock") and (choice != "scissors") and (choice != "paper"):
                print("Invalid choice.")
        else:
            break

    match opponent:
        case "rock":
            match choice:
                case "rock":
                    print(f"Tie! Opponent chose {opponent}")
                case "paper":
                    print(f"You win! Opponent chose {opponent}")
                case "scissors":
                    print(f"You lose! Opponent chose {opponent}")
        case "paper":
            match choice:
                case "rock":
                    print(f"You lose! Opponent chose {opponent}")
                case "paper":
                    print(f"Tie! Opponent chose {opponent}")
                case "scissors":
                    print(f"You win! Opponent chose {opponent}")
        case "scissors":
            match choice:
                case "rock":
                    print(f"You win! Opponent chose {opponent}")
                case "paper":
                    print(f"You lose! Opponent chose {opponent}")
                case "scissors":
                    print(f"Tie! Opponent chose {opponent}")
    play_again = input("Play again? (Y/N)").upper()

print("Thanks for playing!")