import tkinter as tk
from tkinter import ttk
import random
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Scissors" and computer_choice == "Paper") or
        (player_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "You lose!"
def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
def play_again():
    result_label.config(text="Make your choice:")
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
intro_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
intro_label.pack(pady=10)
rock_button = tk.Button(root, text="Rock", command=lambda: [play_game("Rock"), disable_buttons()])
rock_button.pack(side=tk.LEFT, padx=20)
paper_button = tk.Button(root, text="Paper", command=lambda: [play_game("Paper"), disable_buttons()])
paper_button.pack(side=tk.LEFT, padx=20)
scissors_button = tk.Button(root, text="Scissors", command=lambda: [play_game("Scissors"), disable_buttons()])
scissors_button.pack(side=tk.LEFT, padx=20)
result_label = tk.Label(root, text="Make your choice:")
result_label.pack(pady=20)
play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack(pady=20)
def disable_buttons():
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)
root.mainloop()
