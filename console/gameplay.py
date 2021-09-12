from utils.utils import Utils as UTILS
from utils.MESSAGES import Messages as MESSAGES
import utils.CONSTANTS as CONSTANTS

from console.game_board import GameBoard as GameBoard

from models.coordinate_model import CoordinateModel
from models.submarina_a_model import SubmarineAModel as submarine_a
from models.submarine_b_model import SubmarineBModel as submarine_b

class GamePlay:
    
    # Regra: O barco não pode sobrepor outro barco e nem ficar fora do tabuleiro.
    def verify_position_grid( grid, coordinate_y, coordinate_x, verbose=True ):
        if coordinate_x >= CONSTANTS.SIZE or coordinate_y >= CONSTANTS.SIZE or coordinate_x < 0 or coordinate_y < 0:
            if verbose:
                print( "> Embarcação fora do tabuleiro!" ) # ({numtocoord(x)}{y})
            return True
        
        elif grid[coordinate_y][coordinate_x] != " ":
            if verbose:
                print( "> Está posição já esta ocupada!" ) # ({numtocoord(x)}{y})
            return True
        
        else:
            return False
    
    def valid_coordinates( grid, initial_coordinate_y, final_coordinate_y, initial_coordinate_x, final_coordinate_x, verbose=True ):
        i = initial_coordinate_y
        
        while i <= final_coordinate_y:
            j = initial_coordinate_x
            
            while j <= final_coordinate_x:
                if GamePlay.verify_position_grid( grid, i, j, verbose ):
                    return True
                
                j += 1
            i += 1
            
        return False
    
    def position_ship( grid, ship_size, coordinate_model, verbose=True ):
        if coordinate_model.position == "V":
            if not GamePlay.valid_coordinates( grid, coordinate_model.coordinate_y, ( coordinate_model.coordinate_y + ship_size - 1 ), coordinate_model.coordinate_x, coordinate_model.coordinate_x, verbose ):
                # print( f"\t\t ADD: {ship_size}" )
                for i in range( ship_size ):
                    grid[coordinate_model.coordinate_y + i][coordinate_model.coordinate_x] = ship_size
                return True
            else:
                return False
        elif coordinate_model.position == "H":
            if not GamePlay.valid_coordinates( grid, coordinate_model.coordinate_y, coordinate_model.coordinate_y, coordinate_model.coordinate_x, ( coordinate_model.coordinate_x + ship_size - 1 ), verbose ):
                for i in range( ship_size ):
                    grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x + i] = ship_size
                return True
            else:
                return False
        else:
            if not GamePlay.valid_coordinates( grid, coordinate_model.coordinate_y, coordinate_model.coordinate_y, coordinate_model.coordinate_x, coordinate_model.coordinate_x, verbose ):
                for i in range( ship_size ):
                    grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x + i] = ship_size
                return True
            else:
                return False
    
    def insert_coordinate( ship_model, coordinate_model ):
        while coordinate_model.coordinate_x < 0 or coordinate_model.coordinate_y < 0 or coordinate_model.coordinate_x > CONSTANTS.SIZE or coordinate_model.coordinate_y > CONSTANTS.SIZE:
            ship_name = ship_model.ship_name
            
            print( f"\nDigite a coordenada que deseja colocar o {ship_name} ({ship_model.ship_size} casas): \n(exemplo: A1)\n" )
            coordinate = input( "> " )
            
            try:
                coordinate_model.coordinate_x = int( UTILS.letter_to_column_number( coordinate[0].upper() ) )
            except:
                break
            else:
                try:
                    coordinate_model.coordinate_y = int( coordinate[1] )
                except:
                    break
                    
            return coordinate_model
    
    def vertical_or_horizontal():
        position = MESSAGES.QUESTION_HORIZONTAL_OR_VERTICAL().upper()
        
        while ( position != "V" ) and ( position != "H" ):
            position = MESSAGES.QUESTION_WARNING_POSITION().upper()
        
        return position
    
    def insert_ship():
        for ship_model in CONSTANTS.LIST_OF_SHIP_MODELS:
            inserted = False
            submarine_a_model = submarine_a()
            submarine_b_model = submarine_b()
            coordinate_model = CoordinateModel()
            
            while not inserted:
                coordinate_model = GamePlay.insert_coordinate( ship_model, coordinate_model )                
                
                if ship_model.ship_code != submarine_b_model.ship_code and ship_model.ship_code != submarine_a_model.ship_code:
                    coordinate_model.position = GamePlay.vertical_or_horizontal()
                
                temporary_grid = CONSTANTS.GRID_GAME_BOARD
                
                inserted = GamePlay.position_ship( temporary_grid, ship_model.ship_size, coordinate_model )
                
                UTILS.clear()
                GameBoard.draw_game_board( temporary_grid )
                