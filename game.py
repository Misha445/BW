

from player import Player


class Game:
    def __init__(self, player1:Player, player2:Player) -> None:
        
        self.players = [player1, player2]


    def greet(self):
        ...

    def loop(self):
        while True:
            for p in self.players:
                p.move()
                if len(p.opponent_board.ships) == 0:
                    print(p.name, "wins")
                    return

    def start(self):
        for p in self.players:
            p.place_ships()
            print(f"{p.name}")
            p.board.print()
        self.loop()