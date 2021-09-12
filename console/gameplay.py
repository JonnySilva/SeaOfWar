from utils.utils import Utils as UTILS
from utils.MESSAGES import Messages as MESSAGES
import utils.CONSTANTS as CONSTANTS
from console.game_board import GameBoard as GameBoard

class GamePlay:
    
    # Regra: O barco não pode sobrepor outro barco e nem ficar fora do tabuleiro.
    def verify_position_grid( grid, line, column, verbose=True ):
        if column >= CONSTANTS.SIZE or line >= CONSTANTS.SIZE or column < 0 or line < 0:
            if verbose:
                print( "> Embarcação fora do tabuleiro!" ) # ({numtocoord(x)}{y})
            return True
        
        elif grid[line][column] != " ":
            if verbose:
                print( "> Está posição já esta ocupada!" ) # ({numtocoord(x)}{y})
            return True
        
        else:
            return False
    
    def valid_coordinates( grid, initial_line, final_line, initial_column, final_column, verbose=True ):
        i = initial_line
        
        while i <= final_line:
            j = initial_column
            
            while j <= final_column:
                if GamePlay.verify_position_grid( grid, i, j, verbose ):
                    return True
                
                j += 1
            i += 1
            
        return False
    
    def position_ship( grid, ship_size, line, column, isvertical=False, verbose=True ):
        if isvertical:
            if not GamePlay.valid_coordinates( grid, line, ( line + ship_size - 1 ), column, column, verbose ):
                # print( f"\t\t ADD: {ship_size}" )
                for i in range( ship_size ):
                    grid[line + i][column] = ship_size
                return True
            else:
                return False
        else:
            if not GamePlay.valid_coordinates( grid, line, line, column, ( column + ship_size - 1 ), verbose ):
                for i in range( ship_size ):
                    grid[line][column + i] = ship_size
                return True
            else:
                return False
    
    def insert_coordinate( ship_model, column, line ):
        while column < 0 or line < 0 or column > CONSTANTS.SIZE or line > CONSTANTS.SIZE:
            ship_name = UTILS.ship_names_enum(ship_model.ship_name)
            
            print( f"\nDigite a coordenada que deseja colocar o {ship_name} ({ship_model.ship_size} casas): \n(exemplo: A1)\n" )
            coordinate = input( "> " )
            
            try:
                column = int( UTILS.letter_to_column_number( coordinate[0].upper() ) )
            except:
                break
            else:
                try:
                    line = int( coordinate[1] )
                except:
                    break
                    
            return column, line
    
    def vertical_or_horizontal():
        is_vertical = MESSAGES.QUESTION_HORIZONTAL_OR_VERTICAL().upper()
        
        while ( is_vertical != "V" ) and ( is_vertical != "H" ):
            is_vertical = MESSAGES.QUESTION_WARNING_POSITION().upper()
        
        is_vertical = is_vertical == "V"
        
        return is_vertical
    
    def insert_ship():
        for ship_model in CONSTANTS.LIST_OF_SHIP_MODELS:
            placed = False
            column = -1
            line = -1
            is_vertical = ""
            
            while not placed:
                column, line = GamePlay.insert_coordinate( ship_model, column, line )                
                
                is_vertical = GamePlay.vertical_or_horizontal()
                
                temporary_grid = CONSTANTS.GRID_GAME_BOARD
                
                placed = GamePlay.position_ship( temporary_grid, ship_model.ship_size, line, column, is_vertical )
                
                GameBoard.draw_game_board( temporary_grid )
