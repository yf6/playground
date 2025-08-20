#!/usr/bin/env python3
import random

def play_game(num_cups):
    """
    Main logic for a single game round where the user must guess the correct order of the cups.
    """
    print(f"Game started with {num_cups} cups!")

    cups_order = list(range(1, num_cups + 1))
    print(f"Your task is to guess the correct order of the cups (e.g., {' '.join(str(i) for i in cups_order)}).")

    # Shuffled order of cups
    random.shuffle(cups_order)
        
    while True:
        # Get the user's guess for the cup order
        user_input = input(f"Enter your guess for the order: ")
        
        # Cheat to reveal answer
        if user_input == "reveal":
            reveal_answer = input(f"Are you sure you want to reveal the answer? (y/n)")
            if reveal_answer == 'y':
                print(f"The winning order is: {' '.join(str(i) for i in cups_order)}")
                continue

        # Split the input into a list of strings
        guessed_order_str = user_input.split()
        
        # Validate the input
        if len(guessed_order_str) != num_cups:
            print(f"Invalid guess. You must enter {num_cups} numbers.")
            continue
            
        try:
            # Convert the list of strings to a list of integers
            guessed_order = [int(cup) for cup in guessed_order_str]
        except ValueError:
            print("Invalid guess. Please enter only numbers separated by spaces.")
            continue

        # Check for duplicates and if numbers are within the valid range
        if len(set(guessed_order)) != num_cups or any(cup < 1 or cup > num_cups for cup in guessed_order):
            print("Invalid guess. Each cup number (1 to {}) must be used exactly once.".format(num_cups))
            continue
            
        # Count how many cups are in the correct position
        correct_count = 0
        for i in range(num_cups):
            if guessed_order[i] == cups_order[i]:
                correct_count += 1
        
        # Provide feedback to the user
        if correct_count == num_cups:
            print(f"Congratulations! You guessed the correct order!")
            print("----------------------------------------")
            break # Exit the game loop
        else:
            print(f"Number of cups in the correct position: {correct_count}\n")

def main_game_loop():
    """
    The main game loop that controls the flow of the game.
    """
    print("Welcome to the Cup Matching Game! ☕")
    print("----------------------------------------")
    
    while True:
        # Asks the user to input the number of cups for the game.
        user_input = input("Enter the number of cups you want to play with, or q to quit: ")
        if user_input == 'q':
            print("Thanks for playing! Goodbye! 👋")
            break
        
        if user_input.isdigit():
            num_cups = int(user_input)
            play_game(num_cups)
        else:
            print("Invalid input. Please enter a number.")
            
if __name__ == "__main__":
    main_game_loop()