# Rock-Paper-Scissors
import tkinter as tk
import random
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        global user_score
        user_score += 1
        return "You win!"
    else:
        global computer_score
        computer_score += 1
        return "Computer wins!"

# Function to play a round
def play_round(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = determine_winner(user_choice, computer_choice)
    
    # Update labels with the user's and computer's choices
    label_user_choice.config(text=f"Your choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's choice: {computer_choice}")
    
    # Display result
    label_result.config(text=f"Result: {result}")
    
    # Update scores
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Function to restart the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_result.config(text="Result: ")
    label_user_choice.config(text="Your choice: ")
    label_computer_choice.config(text="Computer's choice: ")
    label_score.config(text="Score - You: 0 | Computer: 0")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")

# Initialize scores
user_score = 0
computer_score = 0

# Create labels to display user choice, computer choice, result, and score with effect
label_user_choice = tk.Label(window, text="Your choice: ", font=('Arial', 12), bg="#f0f0f0", bd=3, relief="ridge")
label_user_choice.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

label_computer_choice = tk.Label(window, text="Computer's choice: ", font=('Arial', 12), bg="#f0f0f0", bd=3, relief="ridge")
label_computer_choice.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(window, text="Result: ", font=('Arial', 12), bg="#f0f0f0", bd=3, relief="ridge")
label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

label_score = tk.Label(window, text="Score - You: 0 | Computer: 0", font=('Arial', 12), bg="#f0f0f0", bd=3, relief="ridge")
label_score.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create buttons for user to choose Rock, Paper, or Scissors with effect
button_rock = tk.Button(window, text="Rock", command=lambda: play_round('Rock'), bg="#add8e6", font=('Arial', 12), width=10, bd=5, relief="raised")
button_rock.grid(row=4, column=0, padx=10, pady=10)

button_paper = tk.Button(window, text="Paper", command=lambda: play_round('Paper'), bg="#ffcccb", font=('Arial', 12), width=10, bd=5, relief="raised")
button_paper.grid(row=4, column=1, padx=10, pady=10)

button_scissors = tk.Button(window, text="Scissors", command=lambda: play_round('Scissors'), bg="#d3ffce", font=('Arial', 12), width=10, bd=5, relief="raised")
button_scissors.grid(row=5, column=0, padx=10, pady=10)

# Create a button to reset the game with effect
button_reset = tk.Button(window, text="Reset Game", command=reset_game, bg="#f0e68c", font=('Arial', 12), width=10, bd=5, relief="raised")
button_reset.grid(row=5, column=1, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
