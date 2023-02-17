import random

board = [" " for i in range(9)]


def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))
    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if choice < 1 or choice > 9:
                raise ValueError  # raise ValueError for values outside of 1-9
            if board[choice-1] == " ":
                board[choice-1] = icon
                return True
            else:
                print()
                print("That space is taken!")
                print_board()
                print()
        except (ValueError, IndexError):
            print()
            print("Invalid choice. Please enter a number between 1 and 9.")
            print_board()
            print()


def computer_move(icon):
    if icon == "X":
        other_icon = "O"
    elif icon == "O":
        other_icon = "X"

    # First, check for a winning move
    for i in range(9):
        if board[i] == " ":
            board[i] = icon
            if is_winner(icon):
                return
            else:
                board[i] = " "

    # Second, check for a blocking move
    for i in range(9):
        if board[i] == " ":
            board[i] = other_icon
            if is_winner(other_icon):
                board[i] = icon
                return
            else:
                board[i] = " "

    # Third, try to take one of the corners
    corners = [1, 3, 7, 9]
    random.shuffle(corners)
    for corner in corners:
        if board[corner-1] == " ":
            board[corner-1] = icon
            return

    # Fourth, try to take the center
    if board[4] == " ":
        board[4] = icon
        return

    # Finally, take any edge
    edges = [2, 4, 6, 8]
    random.shuffle(edges)
    for edge in edges:
        if board[edge-1] == " ":
            board[edge-1] = icon
            return


def is_winner(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():
    return " " not in board


while True:
    print_board()
    player_move("X")
    if is_winner("X"):
        print_board()
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print_board()
        print("It's a draw!")
        break

    computer_move("O")
    if is_winner("O"):
        print_board()
        print("O wins! Better luck next time!")
        break
    elif is_draw():
        print_board()
        print("It's a draw!")
        break
