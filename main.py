import tkinter as tk
from tkinter import messagebox

# Initializing the play box
root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = None  # Set to None initially
buttons = [[None, None, None], [None, None, None], [None, None, None]]
game_over = False


# Highlight the winner
def highlight_winner(b1, b2, b3):
    b1.config(bg='lightgreen')
    b2.config(bg='lightgreen')
    b3.config(bg='lightgreen')


# Function to check for the winner
def check_winner():
    global game_over

    # Check the rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            highlight_winner(buttons[row][0], buttons[row][1], buttons[row][2])
            messagebox.showinfo("Game Over", f'Player {buttons[row][0]["text"]} wins!')
            game_over = True
            return

    # Check the columns
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != '':
            highlight_winner(buttons[0][col], buttons[1][col], buttons[2][col])
            messagebox.showinfo("Game Over", f'Player {buttons[0][col]["text"]} wins!')
            game_over = True
            return

    # Check the diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        highlight_winner(buttons[0][0], buttons[1][1], buttons[2][2])
        messagebox.showinfo("Game Over", f'Player {buttons[0][0]["text"]} wins!')
        game_over = True
        return

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != '':
        highlight_winner(buttons[2][0], buttons[1][1], buttons[0][2])
        messagebox.showinfo("Game Over", f'Player {buttons[2][0]["text"]} wins!')
        game_over = True
        return

    # Check for a draw
    if all(buttons[row][col]['text'] != '' for row in range(3) for col in range(3)) and not game_over:
        messagebox.showinfo("Game Over", "The game is a draw!")
        game_over = True
        return


# Button click function
def button_click(row, col):
    global current_player
    if buttons[row][col]['text'] == '' and not game_over and current_player is not None:
        buttons[row][col]['text'] = current_player
        buttons[row][col].config(fg='red' if current_player == 'X' else 'green')

        # Check if there is a winner
        check_winner()

        # Toggle player
        current_player = 'O' if current_player == 'X' else 'X'


# Reset the game
def reset_game():
    global current_player, game_over
    current_player = None
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
            buttons[row][col].config(bg='SystemButtonFace')
    pick_o_button.config(state=tk.NORMAL)
    pick_x_button.config(state=tk.NORMAL)


# Pick character
def pick_char(char):
    global current_player
    current_player = char
    if current_player is not None:
        pick_o_button.config(state=tk.DISABLED)
        pick_x_button.config(state=tk.DISABLED)
    messagebox.showinfo("Character Selected", f"You selected {current_player}. Let's start the game!")


# Create the grid
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(
            root,
            text='',
            width=15,
            height=5,
            font=('Helvetica', 20),
            command=lambda r=row, c=col: button_click(r, c)
        )
        buttons[row][col].grid(row=row, column=col)

# Buttons for picking characters
pick_char_button = tk.Frame(root)
pick_char_button.grid(row=3, column=0, columnspan=3)

pick_x_button = tk.Button(
    pick_char_button,
    text='Pick X',
    font=("Helvetica", 15),
    command=lambda: pick_char('X')
)
pick_x_button.pack(side=tk.LEFT, padx=10)

pick_o_button = tk.Button(
    pick_char_button,
    text='Pick O',
    font=("Helvetica", 15),
    command=lambda: pick_char('O')
)
pick_o_button.pack(side=tk.LEFT, padx=10)

# Reset button
reset_button = tk.Button(
    root,
    text='Restart Game',
    font=("Helvetica", 15),
    command=reset_game
)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
