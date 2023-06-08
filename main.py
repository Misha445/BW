from ai import AI
from game import Game
from ship import Ship
from board import Board, get_ships_count
from user import User

def main():
    user_board = Board()
    ai_board = Board()
    # # b.print()
    # # b.add_ship(Ship(0,0,3,"v"))
    # # b.print()
    ai = AI("ai", ai_board, user_board)
    # bot.place_ships()
    # bot_board.print()
    user = User("user", user_board, ai_board)
    game = Game(ai, user)
    game.start()
    
main()    
