from board import Board

class Player:
    def __init__(self, name:str, board: Board, opponent_board:Board) -> None:
        self.name = name
        self.board = board 
        self.opponent_board = opponent_board

    def place_ships(self):
        self.board.place_ships()

    def move(self):
        ...