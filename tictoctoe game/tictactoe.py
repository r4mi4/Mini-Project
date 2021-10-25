import os

def show_board():
    '''
    show tictactoe board 
    '''
    print(*['{} | {} | {}'.format(*[vertebrae[j] for j in board[i]]) for i in range(3)], sep='\n'+'-'*9+'\n')

def play(i,j):
    board[i][j]=player

def Game_status():
    '''
    Game status 
    '''
    options=[column for column in board] \
        +[[board[i][j] for i in range(3)] for j in range(3)] \
            +[[board[i][i] for i in range(3)]]+[[board[i][2-i] for i in range(3)]]
    for option in options:
        if len(set(option))==1 and list(set(option))[0]!=0:
            return option[0]
    if sum([1 for i in range(3) for j in range(3) if board[i][j]!=0])==9:
        return 3
    return 0

def entranceـnumber():
    '''
    check entries numbers
    '''
    input_i = input('Please Enter i :')
    input_j = input('Please Enter j :')
    if input_i.isdigit() and input_j.isdigit():
        i = int(input_i)
        j= int(input_j)  
        if 0<=i<=2 and 0<=j<=2 and board[i][j] == 0:
            play(i,j)
            return True
    print('you have to use one of these numbers : 0 or 1 or 2')
    return entranceـnumber()

def clean():
    '''
    clean terminal
    '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__  ==  '__main__' :
    board = [[0 for i in range(3)] for j in range(3)]
    vertebrae = [' ', '\033[93mX', '\033[0mO']
    player = 1
    show_board()
    while Game_status() == 0:
        entranceـnumber()
        player = 2 - (player+1)%2    
        clean()
        show_board()  
        
    if Game_status() == 3:
        print('Game Draw')
    else:
        print('Player {} has won !'.format(['X', 'O'][Game_status()- 1]))

