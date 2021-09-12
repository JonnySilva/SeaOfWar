from models.ship_model import AircraftCarrierModel as aircraft_carrier, BattleshipModel as battleship, CruiserModel as cruiser, PatrolShipModel as patrol_ship, SubmarineAModel as submarine_a, SubmarineBModel as submarine_b
import console.game_board as GAMEBOARD
from utils.utils import Utils as UTILS

SIZE = len( GAMEBOARD.GRID_SIZE )
LIST_OF_SHIP_MODELS = [
    
    aircraft_carrier(),
    battleship(),
    cruiser(),
    patrol_ship(),
    submarine_a(),
    submarine_b()
    
]

class GamePlay:
    
    coordinate = []
    column = -1
    line = -1
    is_vertical = ""
    
    def insert_coordinate( ship_model ):
        while GamePlay.column < 0 or GamePlay.line < 0 or GamePlay.column > SIZE or GamePlay.line > SIZE:
            ship_name = UTILS.ship_names_enum(ship_model.ship_name)
            
            print( f"\nDigite a coordenada que deseja colocar o {ship_name} ({ship_model.ship_size} casas): \n(exemplo: A1)\n" )
            while len( GamePlay.coordinate ) < 2:
                GamePlay.coordinate = input( "> " )
                
                try:
                    GamePlay.column = int( UTILS.letter_to_column_number( GamePlay.coordinate[0].upper() ) )
                except:
                    break
                else:
                    try:
                        GamePlay.line = int( GamePlay.coordinate[1] )
                    except:
                        break
    
    def insert_ship():
        for ship_model in LIST_OF_SHIP_MODELS:
            placed = False
            
            while not placed:
                GamePlay.insert_coordinate( ship_model )
                
                is_vertical = input( "Deseja por o navio na vertical? (y/n) \n> " ).upper()
                
                while is_vertical != "Y" and is_vertical != "N":
                    is_vertical = input( "Por favor, selecione 'n' ou 'y': \n> " ).upper()
                    
                GamePlay.is_vertical = is_vertical == "Y"
                