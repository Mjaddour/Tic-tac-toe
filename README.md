# Tic-Tac-Toe Game 

## Overview
This project is a simple **Tic-Tac-Toe** game built using Python's `tkinter` library. It provides a graphical interface where two players can alternate turns to play the classic Tic-Tac-Toe game. Players can choose their symbol (`X` or `O`), and the game highlights the winning line or declares a draw when no more moves are possible.

---

## Features
- **Interactive Gameplay**: Players click buttons to mark their moves.
- **Symbol Selection**: Players can pick either `X` or `O` before starting the game.
- **Winner Highlighting**: Highlights the winning row, column, or diagonal.
- **Draw Detection**: Detects and announces a draw when the board is full.
- **Restart Option**: Reset the game board to play again.

---

## Requirements
- Python 3.x
- `tkinter` library (comes pre-installed with Python)

---

## How to Run
1. Save the script to a file named, for example, `tic_tac_toe.py`.
2. Open a terminal or command prompt.
3. Run the script using:
   ```bash
   python tic_tac_toe.py
   ```

---

## Gameplay Instructions
1. **Start the Game**:
   - A 3x3 grid of buttons will appear, representing the Tic-Tac-Toe board.
   - Two buttons, "Pick X" and "Pick O," allow the first player to choose their symbol.

2. **Play Turns**:
   - Players take turns clicking on the buttons to place their symbol (`X` or `O`).
   - The current symbol is displayed on the buttons, with `X` in red and `O` in green.

3. **Winning the Game**:
   - The first player to get three symbols in a row (horizontally, vertically, or diagonally) wins.
   - The winning line is highlighted in green.

4. **Draw**:
   - If all cells are filled without a winner, a "Game Over" message will display announcing a draw.

5. **Restart the Game**:
   - Click the "Restart Game" button to clear the board and play again.

---

## Code Structure
- **GUI Initialization**:
  - A 3x3 grid of buttons represents the game board.
  - Buttons for symbol selection (`Pick X` and `Pick O`) and restarting the game.
- **Game Logic**:
  - `button_click(row, col)`: Handles button clicks and updates the board.
  - `check_winner()`: Checks for a win or draw condition.
  - `highlight_winner(b1, b2, b3)`: Highlights the winning cells.
  - `reset_game()`: Resets the board for a new game.
- **State Management**:
  - Tracks the current player (`X` or `O`) and whether the game is over.

---

## Customization
- **Button Appearance**: Modify the `width`, `height`, and `font` attributes of the buttons for a different look.
- **Winning Line Color**: Change the `bg='lightgreen'` parameter in `highlight_winner()` to use a different color.

---

## Future Enhancements
- Add an AI opponent for single-player mode.
- Allow players to customize their symbols.
- Add animations for transitions and winning highlights.

---

Enjoy playing Tic-Tac-Toe! 🎮
