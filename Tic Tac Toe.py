# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:43:59 2018

@author: shrivh1
"""

from IPython.display import clear_output
clear_output()


def draw_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
    
def player_input():
    player1 = ''
    player2 = ''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1 choose your marker - X or O : ').upper()
    
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)



import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def check_combination(board,marker):
    return ((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker) or
    (board[1] == board[5] == board[9] == marker) or
    (board[7] == board[5] == board[3] == marker) )



def space_check(board,position):
    return board[position] == ' '
    



def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Player input your choice - 1 to  9 : '))
    return position

#position = player_choice()
#player1_marker,player2_marker= player_input()

#marker = player1_marker

def choice_marker(board, position, marker):
    board[position] = marker

#choice_marker(board,position,marker)
#drawboard(board)



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True



def ask_replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')




print('Welcome to Tic Tac Toe !!')

while True:
    
    board = [' ']* 10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    
    print(turn + ' will start the game .')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            print('you are in P1')
            draw_board(board)
            position = player_choice(board)
            choice_marker(board,position,player1_marker)
            
            if check_combination(board, player1_marker):
                draw_board(board)
                print('Player 1 have won the game')
                game_on = False
            else:
                if full_board_check(board):
                    draw_board(board)
                    print('This is a draw !!')
                    game_on = False
                    break
                else:
                    turn = 'Player 2'
        else:
            print('you are in P2')
            draw_board(board)
            position = player_choice(board)
            choice_marker(board,position,player2_marker)
            
            if check_combination(board,player2_marker):
                draw_board(board)
                print('Player 2 have won the game')
                game_on = False
            else:
                if full_board_check(board):
                    draw_board(board)
                    print('This is a draw !!') 
                    game_on = False
                    break
                else:
                    turn = 'Player 1'
                
    if not ask_replay():
        break


