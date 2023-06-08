from board import Board, get_ships_count
from coordinate import Coordinate
from player import Player
from ship import Ship
from random import choice, randint

class AI(Player):
    def move(self):
        c = Coordinate(randint(0,self.opponent_board.size - 1), randint(0,self.opponent_board.size - 1))
        print(f"ai shoots {c.inc()}")
        r = self.opponent_board.shoot(c)
        print(r)
        self.opponent_board.print()