class SymbolError(Exception):
    pass

def players():
    player_one = input("Please choose between 'O' and 'X':\n").upper()
    player_two = 'O' if player_one == 'X' else 'X'.upper()

    if player_one == 'X' or player_one == "O":
        if player_two == 'X' or player_two == "O":
            return player_one, player_two

    raise SymbolError("Invalid symbol choice!")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None


def check_position(board, position, position_mapper):
    current_indexes = position_mapper[position]
    row_index = current_indexes[0]
    col_index = current_indexes[1]

    if board[row_index][col_index] != "O" and board[row_index][col_index] != "X":
        return True
    else:
        return False

def print_board(board):
    for row in board:
        print(' | '.join(row))

def start():
    player_one,player_two = players()

    winner = None

    position_mapper = {
        1: (0,0),
        2: (0,1),
        3: (0,2),
        4: (1,0),
        5: (1,1),
        6: (1,2),
        7: (2,0),
        8: (2,1),
        9: (2,2),
    }

    board = [[' ' for _ in range (3)] for _ in range(3)]
    empty_positions = 9

    while empty_positions > 0:
        print_board(board)
        try:
            position = int(input("Please choose a position on the board between '1-9':\n"))
        except ValueError:
            print("The position should be digit.")


        if position in position_mapper:
            row_index = position_mapper[position][0]
            col_index = position_mapper[position][1]

            if check_position(board, position, position_mapper):
                if empty_positions % 2 == 0:
                    board[row_index][col_index] = player_two
                else:
                    board[row_index][col_index] = player_one
                empty_positions -= 1
            else:
                print("This position is not empty. Please select a valid position!")
        else:
            print('Invalid position. Please choose a valid position.')

        winner = check_winner(board)
        if winner:
            print(f'The winner is: {winner}')
            print_board(board)
            return winner
        elif empty_positions == 0:
            print_board(board)
            print('Tie game!')
            return winner

points = {
    'X': 0,
    'O': 0,
}
players()
winner = start()

while True:
    if winner:
        points[winner] += 1

    print(f"Player one points: {points['X']}")
    print(f"Player two points: {points['O']}")

    restart = input("Press 'r' to start a new game.\nTo exit press everything else.\n")

    if restart.lower() == 'r':
        start()
    else:
        raise SystemExit

