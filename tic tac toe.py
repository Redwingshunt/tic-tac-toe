def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
        

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        ask = True
        print_board(board)
        while ask: #will be asking till the row and col values are  from 0 to 2
            print(" please choose something from '0'|'1'|'2'")
            row = int(input(f"Player {player}, choose row (0, 1, 2): "))
            col = int(input(f"Player {player}, choose column (0, 1, 2): "))
            if row <=2 and col <=2:
                ask = False    # exiting out of

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("That position is already taken. Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if all(all(cell != ' ' for cell in row) for row in board):
            print_board(board)
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

tic_tac_toe()