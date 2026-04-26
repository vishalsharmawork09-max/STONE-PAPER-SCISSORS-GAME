import random

def show_menu():
    print("\n====== ✊📄✂️ STONE PAPER SCISSOR ======")
    print("1. Play Game")
    print("2. Exit")


def get_computer_choice():
    choices = ["stone", "paper", "scissor"]
    return random.choice(choices)


def decide_winner(user, computer):
    if user == computer:
        return "🤝 It's a Tie!"

    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        return "🏆 You Win!"

    else:
        return "💻 Computer Wins!"


# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        print("\nChoose: stone, paper, scissor")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ["stone", "paper", "scissor"]:
            print("❌ Invalid choice! Try again.")
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)
        print(result)

    elif choice == '2':
        print("👋 Thanks for playing!")
        break

    else:
        print("❌ Invalid option! Try again.")