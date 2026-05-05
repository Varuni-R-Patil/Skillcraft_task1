import random
def play_game():
    print("=" * 45)
    print("        NUMBER GUESSING GAME")
    print("=" * 45)
    print("Select difficulty:")
    print("  1. Easy   (1–50,  10 attempts)")
    print("  2. Medium (1–100,  7 attempts)")
    print("  3. Hard   (1–200,  5 attempts)")
    print("-" * 45)
    difficulty = input("Enter your choice (1/2/3): ").strip()
    if difficulty == "1":
        low, high, max_attempts = 1, 50, 10
    elif difficulty == "3":
        low, high, max_attempts = 1, 200, 5
    else:
        low, high, max_attempts = 1, 100, 7
    secret = random.randint(low, high)
    attempts = 0
    print(f"\nI've picked a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")
    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} — Your guess: "))
        except ValueError:
            print("Please enter a valid integer.\n")
            continue
        if guess < low or guess > high:
            print(f"Out of range! Guess between {low} and {high}.\n")
            continue
        attempts += 1
        if guess == secret:
            print(f"\n🎉 Correct! The number was {secret}.")
            print(f"You got it in {attempts} attempt(s)!")
            break
        elif guess < secret:
            hint = "Too low!"
        else:
            hint = "Too high!"
        remaining_after = max_attempts - attempts
        if remaining_after > 0:
            print(f"{hint} {remaining_after} attempt(s) remaining.\n")
        else:
            print(f"\n❌ Out of attempts! The number was {secret}.")
    print()
    again = input("Play again? (yes/no): ").strip().lower()
    if again in ("yes", "y"):
        play_game()
    else:
        print("Thanks for playing!")
if __name__ == "__main__":
    play_game()
