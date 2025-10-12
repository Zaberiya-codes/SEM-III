import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
winning_score = 3

player_name = input("Enter your name: ")

print(f"\n🎮 Welcome, {player_name}! First to score 3 points wins the game.")
print("Type 'rock', 'paper', or 'scissors' to play.\n")

while user_score < winning_score and computer_score < winning_score:
    user_choice = input("Your choice: ").lower()

    if user_choice not in options:
        print("❌ Invalid choice. Try again.\n")
        continue

    computer_choice = random.choice(options)
    print(f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    print(f"Score — {player_name}: {user_score}, Computer: {computer_score}\n")

# Final Result
if user_score == winning_score:
    print(f"🎉 Congratulations {player_name}, you won the game!")
else:
    print(f"😢 Sorry {player_name}, computer won the game!")
