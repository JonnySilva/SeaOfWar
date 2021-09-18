from utils.utils import Utils as UTILS
from utils.MESSAGES import Messages as MESSAGES
import utils.CONSTANTS as CONSTANTS

from console.game_board import GameBoard as GameBoard

from models.coordinate_model import CoordinateModel
from models.submarina_a_model import SubmarineAModel as submarine_a
from models.submarine_b_model import SubmarineBModel as submarine_b

class GamePlay:
    
    coordinate_model = CoordinateModel()
    
    def has_winner():
        amount_upper_letters_to_player = 0
        amount_upper_letters_to_skynet = 0
        
        for coordinate_y in range( CONSTANTS.SIZE ):
            for coordinate_x in range( CONSTANTS.SIZE ):
                if CONSTANTS.GRID_GAME_BOARD[coordinate_y][coordinate_x].isupper():
                    amount_upper_letters_to_skynet += 1
                if CONSTANTS.GRID_IA[coordinate_y][coordinate_x].isupper():
                    amount_upper_letters_to_player += 1
            
        if amount_upper_letters_to_player == 0:
            return 2
        
        if amount_upper_letters_to_skynet == 0:
            return 1
        
        return 0
    
    # Regra: O barco não pode sobrepor outro barco e nem ficar fora do tabuleiro.
    def verify_position_grid( grid, coordinate_y, coordinate_x, verbose=True ):
        if coordinate_x >= CONSTANTS.SIZE or coordinate_y >= CONSTANTS.SIZE or coordinate_x < 0 or coordinate_y < 0:
            if verbose:
                MESSAGES.MESSAGE_WARNING_SHIP_OUTSIDE()
                GamePlay.coordinate_model.reset()
            return True
        
        elif grid[coordinate_y][coordinate_x] != CONSTANTS.SPACE:
            if verbose:
                MESSAGES.MESSAGE_WARNING_POSITION()
                GamePlay.coordinate_model.reset()
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
    
    def position_ship( grid, ship_model, coordinate_model, verbose=True ):
        if coordinate_model.position == "V":
            if not GamePlay.valid_coordinates( grid, coordinate_model.coordinate_y, ( coordinate_model.coordinate_y + ship_model.ship_size - 1 ), coordinate_model.coordinate_x, coordinate_model.coordinate_x, verbose ):
                # print( f"\t\t ADD: {ship_size}" )
                for i in range( ship_model.ship_size ):
                    grid[coordinate_model.coordinate_y + i][coordinate_model.coordinate_x] = ship_model.ship_code[0]
                return True
            else:
                return False
        elif coordinate_model.position == "H":
            if not GamePlay.valid_coordinates( grid, coordinate_model.coordinate_y, coordinate_model.coordinate_y, coordinate_model.coordinate_x, ( coordinate_model.coordinate_x + ship_model.ship_size - 1 ), verbose ):
                for i in range( ship_model.ship_size ):
                    grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x + i] = ship_model.ship_code[0]
                return True
            else:
                return False
        else:
            if not GamePlay.valid_coordinates( grid, coordinate_model.coordinate_y, coordinate_model.coordinate_y, coordinate_model.coordinate_x, coordinate_model.coordinate_x, verbose ):
                for i in range( ship_model.ship_size ):
                    grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x + i] = ship_model.ship_code[0]
                return True
            else:
                return False
    
    def insert_coordinate( coordinate_model, ship_model=None ):
        while coordinate_model.coordinate_x < 0 or coordinate_model.coordinate_y < 0 or coordinate_model.coordinate_x > CONSTANTS.SIZE or coordinate_model.coordinate_y > CONSTANTS.SIZE:
            if ship_model != None:
                ship_name = ship_model.ship_name
                ship_size = ship_model.ship_size
                
                coordinate = MESSAGES.QUESTION_COORDINATE( ship_name, ship_size )
            else:
                print()
                coordinate = MESSAGES.QUESTION_ATTACK()
                
            try:
                coordinate_model.coordinate_x = int( coordinate[0] ) if UTILS.coordinate_is_digit( coordinate[0] ) else int( UTILS.letter_to_column_number( coordinate[0].upper() ) )
            except:
                break
            else:
                try:
                    coordinate_model.coordinate_y = int( coordinate[1] ) if UTILS.coordinate_is_digit( coordinate[1] ) else int( UTILS.letter_to_column_number( coordinate[1].upper() ) )
                except:
                    break
            
            return coordinate_model
    
    def vertical_or_horizontal():
        position = MESSAGES.QUESTION_HORIZONTAL_OR_VERTICAL().upper()
        
        while ( position != "V" ) and ( position != "H" ):
            position = MESSAGES.QUESTION_WARNING_POSITION().upper()
        
        return position
    
    def position_is_correction( ship_model ):
        option = MESSAGES.QUESTION_CONFIRMATION_COORDINATE().upper()
        
        while ( option != "S" ) and ( option != "N" ):
            option = MESSAGES.QUESTION_WARNING_COORDINATE().upper()
        
        if option == "N":
            MESSAGES.MESSAGE_WARNING_CANCEL_COORDINATE()
            return False
        else: 
            return True
    
    def insert_ship():
        for ship_model in CONSTANTS.LIST_OF_SHIP_MODELS:
            inserted = False
            UTILS.clear()
            
            while not inserted:
                submarine_a_model = submarine_a()
                submarine_b_model = submarine_b()
                GamePlay.coordinate_model.reset()
                
                GameBoard.draw_game_board( CONSTANTS.GRID_GAME_BOARD )
                GamePlay.coordinate_model = GamePlay.insert_coordinate( GamePlay.coordinate_model, ship_model )
                
                if ship_model.ship_code != submarine_b_model.ship_code and ship_model.ship_code != submarine_a_model.ship_code:
                    print()
                    GamePlay.coordinate_model.position = GamePlay.vertical_or_horizontal().upper()
                UTILS.clear()
                temporary_grid = CONSTANTS.GRID_GAME_BOARD
                
                if GamePlay.position_ship( temporary_grid, ship_model, GamePlay.coordinate_model ):
                    GameBoard.draw_game_board( temporary_grid )
                    inserted = GamePlay.position_is_correction( ship_model )
                    if inserted == False:
                        temporary_grid = GameBoard.remove_ship( ship_model.ship_code[0] )
                        print( "\nCoordenada cancelada!\n" )
                    
        return temporary_grid
    