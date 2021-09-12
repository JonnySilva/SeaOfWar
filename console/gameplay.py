from utils.utils import Utils as UTILS
from utils.MESSAGES import Messages as MESSAGES
import utils.CONSTANTS as CONSTANTS
from console.game_board import GameBoard as GameBoard

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
    
    def position_ship( grid, ship_size, coordinate_y, coordinate_x, isvertical=False, verbose=True ):
        if isvertical:
            if not GamePlay.valid_coordinates( grid, coordinate_y, ( coordinate_y + ship_size - 1 ), coordinate_x, coordinate_x, verbose ):
                # print( f"\t\t ADD: {ship_size}" )
                for i in range( ship_size ):
                    grid[coordinate_y + i][coordinate_x] = ship_size
                return True
            else:
                return False
        else:
            if not GamePlay.valid_coordinates( grid, coordinate_y, coordinate_y, coordinate_x, ( coordinate_x + ship_size - 1 ), verbose ):
                for i in range( ship_size ):
                    grid[coordinate_y][coordinate_x + i] = ship_size
                return True
            else:
                return False
    
    def insert_coordinate( ship_model, coordinate_x, coordinate_y ):
        while coordinate_x < 0 or coordinate_y < 0 or coordinate_x > CONSTANTS.SIZE or coordinate_y > CONSTANTS.SIZE:
            ship_name = UTILS.ship_names_enum(ship_model.ship_name)
            
            print( f"\nDigite a coordenada que deseja colocar o {ship_name} ({ship_model.ship_size} casas): \n(exemplo: A1)\n" )
            coordinate = input( "> " )
            
            try:
                coordinate_x = int( UTILS.letter_to_column_number( coordinate[0].upper() ) )
            except:
                break
            else:
                try:
                    coordinate_y = int( coordinate[1] )
                except:
                    break
                    
            return coordinate_x, coordinate_y
    
    def vertical_or_horizontal():
        is_vertical = MESSAGES.QUESTION_HORIZONTAL_OR_VERTICAL().upper()
        
        while ( is_vertical != "V" ) and ( is_vertical != "H" ):
            is_vertical = MESSAGES.QUESTION_WARNING_POSITION().upper()
        
        is_vertical = is_vertical == "V"
        
        return is_vertical
    
    def insert_ship():
        for ship_model in CONSTANTS.LIST_OF_SHIP_MODELS:
            placed = False
            coordinate_x = -1
            coordinate_y = -1
            is_vertical = ""
            
            while not placed:
                coordinate_x, coordinate_y = GamePlay.insert_coordinate( ship_model, coordinate_x, coordinate_y )                
                
                is_vertical = GamePlay.vertical_or_horizontal()
                
                temporary_grid = CONSTANTS.GRID_GAME_BOARD
                
                placed = GamePlay.position_ship( temporary_grid, ship_model.ship_size, coordinate_y, coordinate_x, is_vertical )
                
                UTILS.clear()
                GameBoard.draw_game_board( temporary_grid )
                
