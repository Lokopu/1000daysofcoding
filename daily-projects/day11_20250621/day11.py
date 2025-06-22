import random


def main():
    print("You've activated rock, paper, scissors!")

    player_input = input("Please input ('r' - rock, 'p' - paper or 's' - scissor) to play the game: ")
    if player_input not in ["r", "p", "s"]:
        print("Please input correct letter")
        exit()

    computer_input = random_rps_output()

    print(f"Computer chooses: {computer_input}")

    print(check_winner(player_input, computer_input))



def random_rps_output():
    random_int = random.randint(1, 3)
    if random_int == 1:
        return "r"
    elif random_int == 2:
        return "p"
    elif random_int == 3:
        return "s"
    

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie!"
    if player_choice == "r" and computer_choice == "s":
        return "Human wins!"
    if player_choice == "s" and computer_choice == "r":
        return "Computer wins!"
    if player_choice == "r" and computer_choice == "p":
        return "Computer wins!"
    if player_choice == "p" and computer_choice == "r":
        return "Human Wins!"
    if player_choice == "s" and computer_choice == "p":
        return "Human wins!"
    if player_choice == "p" and computer_choice == "s":
        return "Computer wins!"


if __name__ == "__main__":
    main()