import Piece

class Board():

    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([None]*8)

        #Instantiate white pieces
        self.board[7][0] = Piece.Rook("w")
        self.board[7][1] = Piece.Knight("w")
        self.board[7][2] = Piece.Bishop("w")
        self.board[7][3] = Piece.Queen("w")
        self.board[7][4] = Piece.King("w")
        self.board[7][5] = Piece.Bishop("w")
        self.board[7][6] = Piece.Knight("w")
        self.board[7][7] = Piece.Rook("w")

        for i in range(8):
            self.board[6][i] = Piece.Pawn("w")

        #Instantiate black pieces
        self.board[0][0] = Piece.Rook("b")
        self.board[0][1] = Piece.Knight("b")
        self.board[0][2] = Piece.Bishop("b")
        self.board[0][3] = Piece.Queen("b")
        self.board[0][4] = Piece.King("b")
        self.board[0][5] = Piece.Bishop("b")
        self.board[0][6] = Piece.Knight("b")
        self.board[0][7] = Piece.Rook("b")

        for i in range(8):
            self.board[1][i] = Piece.Pawn("b")


    def draw_board(self):
        
        print(" _____ _____ _____ _____ _____ _____ _____ _____") # top of board
        
        for i in range(8):
            print("|     |     |     |     |     |     |     |     |")
            print("|", end="")
            for j in range(8):
                if self.board[i][j] == None:
                    print("   ",end ="")
                else:
                    if self.board[i][j].get_color() == "b":
                        print("\033[94m  " + self.board[i][j].get_name() + "\033[0m", end="")
                    else:
                        print("  " + self.board[i][j].get_name(), end="")
                print("  |",end="")
            print(" " + str(8 - i)) # Ranks on right side of board
            print("|_____|_____|_____|_____|_____|_____|_____|_____|")

        #Letters are the bottom of board
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(7):
            print("   " + letters[i] + "  ", end="")
        print("   h  ")
        
    def move_piece(self, piece, dest):
        selectedPiece = self.board[piece[0]][piece[1]]
        print(selectedPiece.get_valid_moves(self.board, piece))
        if self.check_castle(selectedPiece, piece, dest):
            self.board[dest[0]][ dest[1]] = selectedPiece
            selectedPiece.has_moved()
            self.board[piece[0]][piece[1]] = None
    def check_castle(self, king, start, dest):
        print('castle check started')
        if king.get_name() == "K" and king.is_first_move():
            print('piece is king and it is the first move')
            print(dest[0])
            if dest[1] == 1 and self.board[start[0]][0]:
                print('king is moving left and a piece exists on the rook square')
                rook = self.board[start[0]][0]
                if rook.get_name() == "R" and rook.is_first_move():
                    print('rook square is a rook and the rook has not moved yet')
                    self.board[dest[0]][dest[1]] = king
                    king.has_moved()
                    self.board[start[0]][start[1]] = None
                    self.board[dest[0]][dest[1] + 1] = rook
                    rook.has_moved()
                    self.board[start[0]][0] = None
                    return False
            if dest[1] == 6 and self.board[start[0]][7]:
                print('king is moving right and a piece exists on the rook square')
                rook = self.board[start[0]][7]
                if rook.get_name() == "R" and rook.is_first_move():
                    self.board[dest[0]][dest[1]] = king
                    king.has_moved()
                    self.board[start[0]][start[1]] = None
                    self.board[dest[0]][dest[1] - 1] = rook
                    rook.has_moved()
                    self.board[start[0]][7] = None
                    return False
        return True

                
                
