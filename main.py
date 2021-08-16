from screens import game_board as gameboard
from screens import players

def main():
    playersList = players.Players.screen()
    gameboard.GameBoard.print_game_board( playersList )

if( __name__ == "__main__" ):
    main()

