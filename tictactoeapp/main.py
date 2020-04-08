from settings import *



def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question):
    # response = None
    # while response not in (low, high):
    response = int(input(question))
    return response



def ask_go_first():
    'спрашивает хочет ли игрок оставить за собой ход первым'
    response = ask_yes_no('Хочешь начать первым? Нажмите Y/N  ')
    if response == 'y':
        human, computer = O, X
        print('Играешь крестиками!)')
    else:
        human, computer = X, O
        print("Играешь нуликами!")
    return human, computer


def make_board():
    board=[]
    for num in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def show_board(board):
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '---------')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '---------')
    print('\t', board[6], '|', board[7], '|', board[8])

def free_moves(board):

    moves = []
    for num in range(NUM_SQUARES):
        if board[num] == EMPTY:
            moves.append(num)
    return moves

def winner(board):
    'определят победителя'
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    free_move = free_moves(board)
    # print(free_move)
    move = None
    while move not in free_move:
        move = ask_number("Выбери позицию куда хочешь сходить от 0 до 8:  ")
        if move > len(board) or move < 0:
            print("Неверный выбор! Выбери снова")
        if move not in free_move:
            print('Это поле занято, выбери другое')
    print(f'Отлично! Ты выбрал {move}')
    return move

def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print('Я выберу ...', end=' ')
    for move in free_moves(board):
        board[move]=computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in free_moves(board):
        board[move]=human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in free_moves(board):
            print(move)
            return move


def next_turn(turn):
    if turn == "X":
        return O
    return X


def main():
    print(instructions.__doc__)
    computer, human = ask_go_first()
    turn = X
    board = make_board()
    show_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, human, computer)
            board[move] = computer
        show_board(board)
        turn = next_turn(turn)
    winner(board)

if __name__ == '__main__':
    main()


