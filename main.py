import Board

def translate(s):
    letters = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7

    }
    return [ 8 - int(s[1]), letters[s[0]]]

chessBoard = Board.Board()
while True:
    chessBoard.draw_board()
    start = translate(input("From: "))

    end = translate(input("To: "))

    chessBoard.move_piece(start, end)