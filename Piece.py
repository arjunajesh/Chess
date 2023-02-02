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
    
    def get_valid_moves(self, x, y):
        pass

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "R"
    #     self.first_move = True
        
    # def is_first_move(self):
    #     return self.first_move
    
    # def has_moved(self):
    #     self.first_move = False

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "K"
    #     self.first_move = True

    # def is_first_move(self):
    #     return self.first_move
    
    # def has_moved(self):
    #     self.first_move = False

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "p"

    def get_valid_moves(self, board, pos):
        valid_moves = []
        i = -1 if self.color == "w" else 1

        print("Available Moves for: " + self.get_name())
        if board[pos[0] + i][pos[1] + 1]:
            if board[pos[0] + i][pos[1] + 1].get_color != self.get_color:
                print("can move diag right")
                valid_moves.append([pos[0] + i, pos[1] + 1])
        if board[pos[0] + i][pos[1] - 1]:
            if board[pos[0] + i][pos[1] - 1].get_color != self.get_color:
                print("got a move diag left")
                valid_moves.append([pos[0] + i, pos[1] - 1])
        if not board[pos[0] + i][pos[1]]:
            print("got a move straight")
            valid_moves.append([pos[0] + i, pos[1]])
            if self.first_move and not board[pos[0] + 2*i][pos[1]]:
                print("got a move straight 2")
                valid_moves.append([pos[0] + 2*i, pos[1]])
        return valid_moves
