# WORDLE Game

A simple Python-based Wordle game where the player has 6 attempts to guess a secret 5-letter word.

## Project Structure
- main.py → Runs the game and handles user input.
- logic.py → Contains the function that checks each letter and determines its color.
- grid.py → Handles the display of the game grid with colors.
- words.txt → Contains the list of possible secret words.

## How to Play
1. The game randomly selects a 5-letter word from `words.txt`.
2. You have 6 attempts to guess the correct word.
3. Color codes:
   - Green: Letter is correct and in the correct position.
   - Yellow: Letter is correct but in the wrong position.
   - Red: Letter is not in the word.

## How to Run
1. Make sure you have Python 3 installed.
2. Place all files (`main.py`, `logic.py`, `grid.py`, `words.txt`) in the same folder.
3. Run the game in the terminal:
   ```bash
   python main.py
