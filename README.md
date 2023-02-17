# Tic Tac Toe

This is a simple command-line implementation of the classic game Tic Tac Toe, also known as Noughts and Crosses.

## Requirements

- Python 3.x

## Getting Started

To play the game, simply run the `tic_tac_toe.py` script in a Python environment. The program will prompt you to make your move by entering a number from 1-9, representing the position on the game board where you want to place your symbol (either "X" or "O"). The game will continue until one player wins, or the game is a draw.

## How to Play

The game is played on a 3x3 board, which is initially empty. The game is played by two players, each of whom is assigned either "X" or "O". Players take turns placing their symbol on the board, with the goal of getting three in a row (either horizontally, vertically, or diagonally).

To make a move, enter a number from 1-9 when prompted. This represents the position on the board where you want to place your symbol, as shown below:

1 | 2 | 3

4 | 5 | 6

7 | 8 | 9

For example, if you want to place your symbol in the top-left corner, enter "1" when prompted.

## Limitations

This implementation of Tic Tac Toe has a few limitations:

- The program doesn't include an AI opponent, so you can only play against another human player.
- The program doesn't include any advanced gameplay features, such as undo or redo moves, or tracking game statistics (e.g. number of wins and draws).
- The program has only basic input validation, so if you enter an invalid input (e.g. a non-integer value, a negative number, or a number outside the range of 1-9), the program will not recognize this and will raise an error.

## Credits

This program was developed by Henry Chan as a simple example of a Python program for playing Tic Tac Toe.

## License

This project is licensed under the [MIT License]. Feel free to use, modify, and distribute the code for any purpose. Please refer to the LICENSE file for more details.
