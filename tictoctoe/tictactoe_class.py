import os

class TicTacToe:
    def __init__(self):
        self.board = [[0 for i in range(3)] for j in range(3)]
        self.vertebrae = [' ', '\033[93mX', '\033[0mO']
        self.player = 1
        self.show_board()
        while self.Game_status() == 0:
            self.entranceـnumber()
            self.player = 2 - (self.player+1)%2    
            self.clean()
            self.show_board()              
        if self.Game_status() == 3:
            print('Game Draw')
        else:
            print('Player {} has won !'.format(['\033[93mX', '\033[0mO'][self.Game_status()- 1]))

    def show_board(self):
        '''
        show tictactoe board 
        '''
        print(*['{} | {} | {}'.format(*[self.vertebrae[j] for j in self.board[i]]) for i in range(3)], sep='\n'+'-'*9+'\n')

    def play(self,i,j):
        self.board[i][j]=self.player

    def Game_status(self):
        '''
        return game status
        '''
        options=[column for column in self.board] \
            +[[self.board[i][j] for i in range(3)] for j in range(3)] \
                +[[self.board[i][i] for i in range(3)]]+[[self.board[i][2-i] for i in range(3)]]
        for option in options:
            if len(set(option))==1 and list(set(option))[0]!=0:
                return option[0]
        if sum([1 for i in range(3) for j in range(3) if self.board[i][j]!=0])==9:
            return 3
        return 0

    def entranceـnumber(self):
        '''
        check entries numbers
        '''
        input_i = input('Please Enter i :')
        input_j = input('Please Enter j :')
        if input_i.isdigit() and input_j.isdigit():
            i = int(input_i)
            j= int(input_j)  
            if 0<=i<=2 and 0<=j<=2 and self.board[i][j] == 0:
                self.play(i,j)
                return True
        print('you have to use one of these numbers : 0 or 1 or 2')
        return self.entranceـnumber()

    def clean(self):
        '''
        clean terminal
        '''       
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
TicTacToe()