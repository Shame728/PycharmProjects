import random


def create_board():
    numbers = shuffle_board([int(i) for i in range(1, 16)]) + [0]
    board = [numbers[i * 4:(i + 1) * 4] for i in range(4)]
    return board

def find_empty(board):
    for x in range(4):
        for y in range(4):
            if board[x][y] == 0:
                return x, y
    return None

def print_board(board):
    print("+~~~" * 4 + "+")
    for row in board:
        line = "|"
        for val in row:
            if val == 0:
                line += "   |"
            else:
                line += f"{val:^3}|"
        print(line)
        print("+~~~" * 4 + "+")

def possible_moves(board):
    x, y = find_empty(board)
    res = []
    if x - 1 >= 0:
        res.append('w')
    if x + 1 <= 3:
        res.append('s')
    if y - 1 >= 0:
        res.append('a')
    if y + 1 <= 3:
        res.append('d')
    ress = ','.join(res)
    return ress


def move(board, go):
    x, y = find_empty(board)
    if go == 'w':
        board[x][y] = board[x - 1][y]
        board[x - 1][y] = 0
    elif go == 's':
        board[x][y] = board[x + 1][y]
        board[x + 1][y] = 0
    elif go == 'a':
        board[x][y] = board[x][y - 1]
        board[x][y - 1] = 0
    elif go == 'd':
        board[x][y] = board[x][y + 1]
        board[x][y + 1] = 0
    return board



def is_winner(board):
    target = [int(i) for i in range(1, 16)] + [0]
    flag = [num for row in board for num in row]
    return target == flag

def shuffle_board(board):
    random.shuffle(board)
    return board
print('игра пятнашки')
how = 1
board = create_board()
while True:
    print_board(board)
    print(f'ход номер: {how}')
    print(f'возможные ходы:{possible_moves(board)}')
    go = str(input())
    if go == 'q':
        print('вы уверены, что хотите покинуть игру? y/n')
        flag = input()
        if flag == 'y':
            break
        if flag == 'n':
            continue
        else:
            print('повторите попытку')
    if go not in possible_moves(board):
        print('такого хода не существует')
    else:
        board = move(board, go)
        how += 1
    if is_winner(board):
        print('победа')
        print(f'количество ходов:{how}')
        break
