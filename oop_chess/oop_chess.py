from pieces import Bishop, Player, Rook, Knight, King, Queen, Pawn

FILES = 'abcdefgh'
RANKS = '12345678'

class ChessBoard:
    _instance = None
    def __new__(cls, *args,**kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls,*args, **kwargs)
            cls._instance.is_initiated = False
        return cls._instance        

    def __init__(self):
        if not self.is_initiated:
            self.is_initiated = True
            self.turn = Player.WHITE
            self.__chess_board = {str(rank):{file : '.' for file in FILES} for rank in RANKS}
            self.__chess_board['2'] = {file : Pawn(Player.WHITE) for file in FILES}
            self.__chess_board['7'] = {file : Pawn(Player.BLACK) for file in FILES}
            self.__chess_board['1'] = { 'a': Rook(Player.WHITE),
                                        'b': Knight(Player.WHITE),
                                        'c': Bishop(Player.WHITE),
                                        'd': Queen(Player.WHITE), 
                                        'e': King(Player.WHITE), 
                                        'f': Bishop(Player.WHITE), 
                                        'g': Knight(Player.WHITE), 
                                        'h': Rook(Player.WHITE)} 
            self.__chess_board['8'] = { 'a': Rook(Player.BLACK),
                                        'b': Knight(Player.BLACK),
                                        'c': Bishop(Player.BLACK),
                                        'd': Queen(Player.BLACK), 
                                        'e': King(Player.BLACK), 
                                        'f': Bishop(Player.BLACK), 
                                        'g': Knight(Player.BLACK), 
                                        'h': Rook(Player.BLACK)} 

    def __repr__(self):
        text = ''
        for rank in self.__chess_board:
            line = ' '.join(map(str, self.__chess_board[rank].values()))
            text +=  f'\033[31;1m{rank :<2}\033[0m{line} \n'
        text += '  \033[32;2ma b c d e f g h\033[0m' 
        return text

    def __getitem__(self,loc: str):
        file, rank=loc
        return self.__chess_board[rank][file]
    
    def __setitem__(self,loc , value):
        file, rank = loc
        self.__chess_board[rank][file] = value

    def move_piece(self,start,stop):

        if self.turn  == Player.WHITE and str(self[start]).isupper():
            raise Exception

        elif self.turn == Player.BLACK and str(self[stop]).islower():
            raise Exception

        self.turn = Player.BLACK if self.turn == Player.WHITE else Player.WHITE
        # self[stop]=self[start]
        # self[start]='.'
        self[start].move_
chess_board=ChessBoard()
# chess_board['h7']['']
# print(chess_board['h7'])
chess_board.move_piece('h7','h5')
chess_board.move_piece('a2','a4')
chess_board.move_piece('g7','g5')
chess_board.move_piece('c2','c3')
print(chess_board)
