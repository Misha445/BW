from coordinate import Coordinate

class Ship:
    #   (в конструктор передаём информацию о его положении на доске).
    def __init__(self, i:int, j:int, length:int, orientation:str):
        self.i = i
        self.j = j
        self.length = length
        orientation = orientation[0].lower()
        if orientation not in "hv":
            raise ValueError("wrong orientation")
        self.orientation = orientation
        self.hits = set()
        self.cells = self._get_cells()

    def _get_cells(self)->list[Coordinate]:
        cells = []
        c = Coordinate(self.j, self.i)
        cells.append(c)
        for i in range(1, self.length):
            c = get_next_cell(c, self.orientation)
            cells.append(c)
        return cells
        
    def hit(self, c:Coordinate):
        self.hits.add(c)

    def is_dead(self):
        return len(self.hits) == len(self.cells)





def toggle_orientation(ship:Ship)->Ship:
    o = "h" if ship.orientation  == "v" else "v" 
    return Ship(ship.i, ship.j, ship.length, o)



def get_next_cell(c:Coordinate, o:str)->Coordinate:
    if o == "h":
        return Coordinate(c.x + 1, c.y)
    elif o == "v":   
        return Coordinate(c.x, c.y + 1)
    raise ValueError("wrong orientation: " + o)
