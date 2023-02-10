class Piece():
    def __init__(self, color):
        self.name = ""
        self.color = color
        self.first_move = True
    
    def is_first_move(self):
        return self.first_move

    def has_moved(self):
        self.first_move = False

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name
    
    def is_valid_move(self, k, m ,s):
        return True
    def get_valid_moves(self, x, y):
        pass
    def check_diag_move(self, board, pos, dest):
        m = [dest[0] - pos[0], dest[1] - pos[1]]
        if abs(m[0]) != abs(m[1]):
            #print("not on diagonal")
            #print(m)
            return False

        m = [int(m[0]/abs(m[0])), int(m[1]/abs(m[1]))]
        #print("direction:")
        #print(m)
        newPos = pos
        while newPos != dest:
            if newPos != pos and board[newPos[0]][newPos[1]] != None:
                #print("found piece in the way")
                return False
            newPos = [newPos[0] + m[0], newPos[1] + m[1]]
        return not board[newPos[0]][newPos[1]] or board[newPos[0]][newPos[1]]!= self.get_color
    def check_straight_move(self, board, pos, dest):
        m = [dest[0] - pos[0], dest[1] - pos[1]]
        if m[0] != 0 and m[1] != 0:
            print("not on a file or rank")
            return False

        if m[0] == 0:
            m[1] = int(m[1]/abs(m[1]))
        else:
            m[0] = int(m[0]/abs(m[0]))
        print(m)
        newPos = pos
        while newPos != dest:
            if newPos != pos and board[newPos[0]][newPos[1]] != None:
                print("found piece in the way")
                return False
            newPos = [newPos[0] + m[0], newPos[1] + m[1]]
        return not board[newPos[0]][newPos[1]] or board[newPos[0]][newPos[1]]!= self.get_color

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "R"
    
    def is_valid_move(self, board, pos, dest):
        return self.check_straight_move(board.board, pos, dest)
        


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"

    def is_valid_move(self, board, pos, dest):
        return dest in self.get_moves(board, pos)

    def get_moves(self,board, pos):
        directions = [[2,1], [2,-1], [-2, 1], [-2,-1], [1,2], [1,-2], [-1,2],[-1,-2]]
        moves = []
        for dir in directions:
            move = [pos[0] + dir[0], pos[1] + dir[1]]
            if board.square_on_board(move) and (not board.board[move[0]][move[1]] or board.board[move[0]][move[1]].get_color() != self.get_color()):
                moves.append(move)
        return moves


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"

    def is_valid_move(self, board, pos, dest):
        return self.check_diag_move(board.board, pos, dest)
            


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"
    
    def is_valid_move(self, board, pos, dest):
        return self.check_diag_move(board.board, pos, dest) or self.check_straight_move(board.board, pos, dest)

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "K"
    
    def is_valid_move(self, board, pos, dest):
        dirs = [-1 , 0 , 1]
        for x in dirs:
            for y in dirs:
                sq = [pos[0] + x, pos[1] + y]
                if dest == sq:
                    return not board.board[dest[0]][dest[1]] or board.board[dest[0]][dest[1]].get_color() != self.get_color()
        return False




class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "p"

    def is_valid_move(self, board, pos, dest):
        return dest in self.get_valid_moves(board.board, pos)
            

    def get_valid_moves(self, board, pos):
        valid_moves = []
        i = -1 if self.color == "w" else 1

        #print("Available Moves for: " + self.get_name())
        if board[pos[0] + i][pos[1] + 1]:
            if board[pos[0] + i][pos[1] + 1].get_color != self.get_color:
                #print("can move diag right")
                valid_moves.append([pos[0] + i, pos[1] + 1])
        if board[pos[0] + i][pos[1] - 1]:
            if board[pos[0] + i][pos[1] - 1].get_color != self.get_color:
                #print("got a move diag left")
                valid_moves.append([pos[0] + i, pos[1] - 1])
        if not board[pos[0] + i][pos[1]]:
            #print("got a move straight")
            valid_moves.append([pos[0] + i, pos[1]])
            if self.first_move and not board[pos[0] + 2*i][pos[1]]:
                #print("got a move straight 2")
                valid_moves.append([pos[0] + 2*i, pos[1]])
        return valid_moves
