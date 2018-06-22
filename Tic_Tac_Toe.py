import random

def display_the_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def choose_marker_to_play():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Choose your marker X or O: ').upper()

    player1 = marker

    if marker.upper() == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

def choose_first_player():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def add_marker_to_board(board, marker, position):
    board[position] = marker

def space_check_in_board(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check_in_board(board, i):
            return False
    return True

def position_check_in_board(board, position):

    while position not in [1,2,3,4,5,6,7,8,9] and not space_check_in_board(board, position):
        position = int(input('Choose your position 1-9 : '))
        
    return position

def game_win_check(board, mark):
    return (
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark) 
            )

    
def start_new_game():
    return input('Do you want to start new game Yes or No? : ').lower().startswith('y')
        

print('XOXOXOXOXOXOXOXOXOXOXOXOXOXO Tic Tac Toe XOXOXOXOXOXOXOXOXOXOXOXOXOXO')

    

    
    

