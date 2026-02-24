import random

def play_game():
    target = random.randint(1, 100)
    attempts = 7
    
    print("\nI'm thinking of a number between 1-100. You have 7 tries.")
    
    for i in range(1, attempts + 1):
        guess = int(input(f"Attempt {i}: Enter guess: "))
        
        if guess == target:
            print(f"Congrats! You won in {i} attempts!")
            return
        elif guess < target:
            print("Too low!")
        else:
            print("Too high!")
            
    print(f"Game Over! The number was {target}.")

while True:
    play_game()
    if input("Play again? (y/n): ").lower() != 'y': break