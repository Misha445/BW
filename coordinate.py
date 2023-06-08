class Coordinate:
    def __init__(self, x:int = -1, y:int = -1, s:str="") -> None:
        if s !="":
            p = s.split()
            self.__init__(int(p[0]), int(p[1]))
            return
        
        self.x = x
        self.y = y

    def __eq__(self, __value: object) -> bool:
        if __value == None:
            return False
        return self.x == __value.x and self.y == __value.y
    
    def __hash__(self) -> int:
        return self.x*self.y + self.y

    def __str__(self):
        return f"({self.x}:{self.y})"
    
    def __repr__(self):
        return str(self) 
    
    def inc(self):      
        
        return Coordinate(self.x+1, self.y+1)