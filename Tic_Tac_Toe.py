def print_grid(board):
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")


def make_move(board):
    while True:
        coords = input("Enter the coordinates: ").split()
        if len(coords) != 2:
            print("You should enter two numbers!")
            continue
        x, y = coords
        if not (x.isdigit() and y.isdigit()):
            print("You should enter numbers!")
            continue
        x, y = int(x), int(y)
        if not (1 <= x <= 3 and 1 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if board[x - 1][y - 1] != '_':
            print("This cell is occupied! Choose another one!")
            continue
        return x - 1, y - 1


def has_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return row[0]
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return board[0][2]
    # no winner
    return None


def is_draw(board):
    for row in board:
        for cell in row:
            if cell == '_':
                return False
    return True


board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

print_grid(board)

current_player = 'X'

while True:
    x, y = make_move(board)
    board[x][y] = current_player
    print_grid(board)
    winner = has_winner(board)
    if winner is not None:
        print(f"{winner} wins")
        break
    if is_draw(board):
        print("Draw")
        break
    current_player = 'X' if current_player == 'O' else 'O'