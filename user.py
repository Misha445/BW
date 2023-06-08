from board import get_ships_count
from coordinate import Coordinate
from player import Player
from ship import Ship

class User(Player): 
        
    def place_ships2(self): 
        ships = get_ships_count()
        # cells_required = sum([l*c for l,c in ships.items()])
        for length, c in ships.items():
            for j in range(c):
                self.input_ship(length)

    def input_ship(self, length:int):

        self.board.print()
        s = input(f"enter coordinates for the ship with length = {length} (x y): " )
        
        p = s.split()
        c = Coordinate(int(p[0]) - 1, int(p[1]) - 1)
        if length == 1:
            o = "v"
        else:
            o = input("enter orientation (h/v): ")
        ship = Ship(c.y, c.x, length, o)
        self.board.add_ship(ship)


    def move(self):
        self.opponent_board.print(False)
        s = input(f"enter coordinates for shoot (x y): " )
        p = s.split()
        c = Coordinate(int(p[0]) - 1, int(p[1]) - 1)
        r = self.opponent_board.shoot(c)
        print(r)