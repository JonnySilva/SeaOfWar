import string
import utils.CONSTANTS as CONSTANTS

class GameBoard:
    
    def generate_space( amount, final ):
        print( f'{CONSTANTS.SPACE * int( amount )}', end=final )
    
    def draw_line():
        print( f'{CONSTANTS.CONST_LINE * int( CONSTANTS.GRID_WIDTH )}', end=CONSTANTS.EMPTY )
    
    def draw_line_top( spaces=0 ):
        GameBoard.generate_space( spaces, CONSTANTS.EMPTY )
        print( CONSTANTS.CONST_CORNER_TOP_LEFT, end=CONSTANTS.EMPTY )
        
        for square_top in range( len( CONSTANTS.GRID_SIZE ) ):
            GameBoard.draw_line()
            print( CONSTANTS.CONST_CORNER_TOP_RIGHT if square_top == 9 else CONSTANTS.CONST_TOP_SEPARATOR, end=CONSTANTS.EMPTY )
    
    def draw_line_mid( spaces=0 ):
        GameBoard.generate_space( spaces, CONSTANTS.EMPTY )
        print( CONSTANTS.CONST_COLUMN_LEFT, end=CONSTANTS.EMPTY )
        
        for square_mid in range( len( CONSTANTS.GRID_SIZE ) ):
            GameBoard.draw_line()
            print( CONSTANTS.CONST_COLUMN_RIGHT if square_mid == 9 else CONSTANTS.CONST_COLUMN_MID, end=CONSTANTS.EMPTY )
    
    def draw_line_bottom( spaces=0 ):
        GameBoard.generate_space( spaces, CONSTANTS.EMPTY )
        print( CONSTANTS.CONST_CORNER_BOTTOM_LEFT, end=CONSTANTS.EMPTY )
        
        for square_bottom in range( len( CONSTANTS.GRID_SIZE ) ):
            GameBoard.draw_line()
            print( CONSTANTS.CONST_CORNER_BOTTOM_RIGHT if square_bottom == 9 else CONSTANTS.CONST_BOTTOM_SEPARATOR, end=CONSTANTS.EMPTY )
    
    def draw_game_board( grid=None ):
        # grid = grid if grid == None else GRID_GAME_BOARD
        
        if grid == None:
            grid = CONSTANTS.GRID_GAME_BOARD
        
        for column in range( len( grid ) ):
            if column == 0:
                GameBoard.generate_space( 2, CONSTANTS.EMPTY )
            
            GameBoard.generate_space( 2, CONSTANTS.EMPTY )
            print( string.ascii_uppercase[column], end=CONSTANTS.EMPTY ) # printing letters/columns (A-J) in the terminal..
            GameBoard.generate_space( 1, CONSTANTS.EMPTY )
        
        print()
        GameBoard.draw_line_top( 2 )
        print()
        
        for line in range( len( grid ) ):
            print( line, end=CONSTANTS.SPACE )
            
            for width in range( len( grid ) ):
                print( CONSTANTS.CONST_MID_SEPARATOR, end=CONSTANTS.EMPTY )
                print( f'{CONSTANTS.SPACE}{grid[line][width]}{CONSTANTS.SPACE}', end=CONSTANTS.EMPTY )
                
            print( CONSTANTS.CONST_MID_SEPARATOR )
            
            if line != 9:
                GameBoard.draw_line_mid( 2 )
                print()
        
        GameBoard.draw_line_bottom( 2 )
        print()
    