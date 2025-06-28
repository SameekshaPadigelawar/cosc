import random
import time
import sys

def roll_dice():
    print("Rolling the die", end="", flush=True)
    
    # Simulate countdown animation
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
    
    # Generate and show the dice result
    result = random.randint(1, 6)
    print(f"\n🎲 You rolled a {result}!\n")

# Main program
print("🎲 Press Enter to roll the die (or type 'q' to quit):")

while True:
    user_input = input(">> ")
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    else:
        roll_dice()
        print("Press Enter to roll again or 'q' to quit.")
