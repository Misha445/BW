from random import choice
from ship import Ship, toggle_orientation
from coordinate import Coordinate
class Board:
    def __init__(self, size = 6) -> None:
        self.size = size
        self.clear()
        
    def clear(self):
        self.ships = []
        self._board = []
        for i in range(self.size):
            row = [0] * self.size
            # for j in range(size):
            #     row[j] = 0
            self._board.append(row)

    def add_ship(self, ship:Ship):
        # 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку. 
        count = sum(1 for s in self.ships if s.length == ship.length )
        if ship.length == 3 and count != 0:
            raise ValueError("1 корабль на 3 клетки уже есть на поле")
        elif ship.length == 2 and count >= 2:
            raise ValueError("2 корабля на 2 клетки уже есть на поле")
        elif ship.length == 1 and count >= 4:
            raise ValueError("4 корабля на одну клетку уже есть на поле")        
        
        cells = ship.cells
        if cells[-1].x >= self.size or cells[-1].y >= self.size:
            raise ValueError("не влезает") 
        # self.assert_distance(ship)

        for c in cells:
            if not self.cell_is_empty(c):
                self.print()
                print(cells)
                print(c)
                raise ValueError(f"cell is not empty: {self.get_cell_value(c)}")
        for c in cells:
            self.set_cell(c, "■")

        self.set_contour(ship)
        self.ships.append(ship)

    def get_cell_value(self, c:Coordinate):
        return self._board[c.y][c.x]
 
    def set_contour(self, ship:Ship):
        if ship.orientation == "h":
            c = self.get_hcontour(ship.cells)
        elif ship.orientation == "v":
            c = self.get_wcontour(ship.cells)
        else:
            raise ValueError("udefined orentation")
                
        contour = [n for n in c if n != None]
        for c in contour:
            self.set_cell(c,'c')

    def get_hcontour(self, cells:list[Coordinate]):
        all = [
            self.get_left_neighbour(cells[0]),
            self.get_upper_left_neighbour(cells[0]),
            self.get_bottom_left_neighbour(cells[0]),
            self.get_right_neighbour(cells[-1]),
            self.get_upper_right_neighbour(cells[-1]),
            self.get_bottom_right_neighbour(cells[-1])]

        for c in cells:
            all.append(self.get_upper_neighbour(c)) 
            all.append(self.get_bottom_neighbour(c))  

        return all
        
    def get_wcontour(self, cells:list[Coordinate]):
        all = [
            self.get_upper_left_neighbour(cells[0]),
            self.get_upper_neighbour(cells[0]),
            self.get_upper_right_neighbour(cells[0]),

            self.get_bottom_right_neighbour(cells[-1]),
            self.get_bottom_left_neighbour(cells[-1]),
            self.get_bottom_neighbour(cells[-1])]
 
        for c in cells:
            all.append( self.get_left_neighbour(c))  
            all.append(self.get_right_neighbour(c))
        return all
    
    def set_cell(self, c: Coordinate, value):
        self._board[c.y][c.x] = value

    def assert_distance(self, ship:Ship):
        # Корабли должны находится на расстоянии минимум одна клетка друг от друга
        for c in ship.cells:
            if not self.cell_is_empty(c):
                raise ValueError(f"клетка {c} уже занята")
            for n in self.get_neighbours(c):
                if self.contains_ship(n):
                    raise ValueError(f"Корабли должны находится на расстоянии минимум одна клетка друг от друга")
            
    def cell_is_empty(self, c:Coordinate)-> bool:
        return self._board[c.y][c.x] == 0
    
    def contains_ship(self, c:Coordinate)-> bool:
        return self._board[c.y][c.x] == "■"
    
    def get_left_neighbour(self, c: Coordinate)->Coordinate:
        if c.x > 0:
            return Coordinate(c.x - 1, c.y)
        return None
    
    def get_right_neighbour(self, c: Coordinate)->Coordinate:
        if c.x < self.size - 1 :
            return Coordinate(c.x + 1, c.y)        
        return None
    
    def get_upper_neighbour(self, c: Coordinate)->Coordinate:
        if c.y > 0:
            return Coordinate(c.x, c.y - 1)      
        return None
    
    def get_upper_left_neighbour(self, c: Coordinate)->Coordinate:
        if c.x > 0 and c.y > 0:
            return Coordinate(c.x - 1, c.y - 1)      
        return None
    
    def get_bottom_left_neighbour(self, c: Coordinate)->Coordinate:
        if c.x > 0 and c.y < self.size - 1:
            return Coordinate(c.x - 1, c.y + 1)  
        return None
    
    def get_bottom_neighbour(self, c: Coordinate)->Coordinate:
        if c.y < self.size - 1:
            return Coordinate(c.x, c.y + 1)
        return None
    
    def get_upper_right_neighbour(self, c: Coordinate)->Coordinate:
        if c.x < self.size - 1 and c.y > 0:
            return Coordinate(c.x + 1, c.y - 1)
        return None
    def get_bottom_right_neighbour(self, c: Coordinate)->Coordinate:
        if c.x < self.size - 1 and c.y  < self.size - 1:
            return Coordinate(c.x + 1, c.y + 1)
        return None


    def get_neighbours(self, c:Coordinate)->list[Coordinate]:

        all = [self.get_upper_left_neighbour(c),
               self.get_left_neighbour(c),
               self.get_bottom_left_neighbour(c),
               self.get_upper_neighbour(c),
               self.get_bottom_neighbour(c),
               self.get_upper_right_neighbour(c),
               self.get_right_neighbour(c),
               self.get_bottom_right_neighbour(c)]

        not_empty = [n for n in all if n != None]
        return not_empty
    

    def print(self, own=True):
        print(end=" |")
        for i in range(1, self.size + 1):
            print(i, end="|")
        print()

        for i in range(self.size):
            print(i+1, end="|")
            for j in range(self.size):
                if not own and (self._board[i][j] not in (0,'T','X')):
                    print('0', end="|")
                else:
                    print(self._board[i][j], end="|")
            print()
            
        print()


    def get_empty_cells(self)->list[Coordinate]:
        r = []
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                c = Coordinate(j, i)                
                if self.cell_is_empty(c):
                    r.append(c)
        return r
    

    
    def place_ships(self):
        for k in range(100000):
            if self.try_add_all_ships():
                return
        raise Exception("failed to place ships")

    def try_add_all_ships(self)->bool:
        ships = get_ships_count()
        cells_required = sum([l*c for l,c in ships.items()])
        self.clear()
        for length, c in ships.items():
            for j in range(c):
                if not self.try_add_one_ship(length):
                    return False
                cells_required -= length
                if len(self.get_empty_cells()) < cells_required:
                    return False
        return True
                

    def try_add_one_ship(self, length)->bool:  
        empty_cells = self.get_empty_cells()     
        while len(empty_cells) >= length:
            c = choice(empty_cells)
            empty_cells.remove(c)
            o = choice(["h","v"]) 
            ship = Ship(c.y, c.x, length, o)
            if self.try_add_ship(ship):
                return True

            if length == 1:
                return False
            
             
            if self.try_add_ship(toggle_orientation(ship)):
                return True
        # self.board.print()
        return False

    def try_add_ship(self, ship):
        if ship.cells[-1].x >= self.size or ship.cells[-1].y >= self.size :
            return False
            # self.add_ship(ship)
            # # self.print()
            # return True

        try:
            self.add_ship(ship)
            # self.print()
            return True
        except:
            ...
            # self.print()    

    def shoot(self, c:Coordinate):
        value =  self._board[c.y][c.x]
        if  value == "■":
            ship = self.get_ship(c)
            ship.hit(c)
            self.set_cell(c, 'X')
            if ship.is_dead():
                self.ships.remove(ship)
                return "killed"
            else:
                return "wounded"
        self.set_cell(c, 'T')
        return "miss"
    
    def get_ship(self, c:Coordinate)->Ship:
        for s in self.ships:
            for x in s.cells:
                if x == c:
                    return s
        return None




def get_ships_count():
    # 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.
    return {3:1, 2:2, 1:4}