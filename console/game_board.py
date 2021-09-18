from random import randint
import string
import utils.CONSTANTS as CONSTANTS

class GameBoard:
    
    human_lifes = [False,False,False,False,False,False]
    skynet_lifes = [False,False,False,False,False,False]

    # Draw table ---------------------
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
    # -------------------------------
    
    def draw_game_board( grid=None ):
        for coordinate_x in range( len( grid ) ):
            if coordinate_x == 0:
                GameBoard.generate_space( 2, CONSTANTS.EMPTY )
            
            GameBoard.generate_space( 2, CONSTANTS.EMPTY )
            print( string.ascii_uppercase[coordinate_x], end=CONSTANTS.EMPTY ) # printing letters/columns (A-J) in the terminal..
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
        
    def draw_life( grid, ships):
        SHIP_REFERENCE = ["S", "M", "B", "G", "T", "R"]
        
        for i in range( len( SHIP_REFERENCE ) ):
            ships[i] = True
        
        for x in range( CONSTANTS.SIZE ):
            for y in range( CONSTANTS.SIZE ):
                if grid[y][x] == "S":
                    ships[0] = False
                if grid[y][x] == "M":
                    ships[1] = False
                if grid[y][x] == "B":
                    ships[2] = False
                if grid[y][x] == "G":
                    ships[3] = False
                if grid[y][x] == "T":
                    ships[4] = False
                if grid[y][x] == "R":
                    ships[5] = False
        
        print( CONSTANTS.SPACE, end=CONSTANTS.EMPTY )
        
        for i in range( len( SHIP_REFERENCE ) ):
            print( SHIP_REFERENCE[i] + CONSTANTS.SPACE, end=CONSTANTS.EMPTY )
            
            if ships[i]:
                print( "\u2661", end=CONSTANTS.SPACE )
            else:
                print( "\u2665", end=CONSTANTS.SPACE )
                
        print()
    
    def invisible_board( grid ):
        for coordinat_y in range( len( grid ) ):
            for coordinate_x in range( len( grid[coordinat_y] ) ):
                if grid[coordinat_y][coordinate_x] == "*":
                    CONSTANTS.PUBLIC_GRID[coordinat_y][coordinate_x] = "*"
                
                elif grid[coordinat_y][coordinate_x].islower():
                    CONSTANTS.PUBLIC_GRID[coordinat_y][coordinate_x] = "o"
                
                else:
                    CONSTANTS.PUBLIC_GRID[coordinat_y][coordinate_x] = " "
        
        return CONSTANTS.PUBLIC_GRID
    
    def remove_ship( letter_ship ):
        for coordinate_y in range( CONSTANTS.SIZE ):
            for coordinate_x in range( CONSTANTS.SIZE ):
                if CONSTANTS.GRID_GAME_BOARD[coordinate_y][coordinate_x] == letter_ship.upper():
                    CONSTANTS.GRID_GAME_BOARD[coordinate_y][coordinate_x] = " "
        
        return CONSTANTS.GRID_GAME_BOARD
    
    def generate_game_board( grid1=None, grid2=None ):
        # grid = grid if grid == None else GRID_GAME_BOARD
        
        if grid1 != None and grid2 != None:
            GameBoard.draw_game_board( grid1 )
            GameBoard.draw_life( grid1, GameBoard.human_lifes )
            GameBoard.draw_game_board( GameBoard.invisible_board( grid2 ) )
            GameBoard.draw_life( grid2, GameBoard.skynet_lifes )
        
        elif grid1 != None and grid2 == None:
            if grid1 == None:
                grid1 = CONSTANTS.GRID_GAME_BOARD
            
            GameBoard.draw_game_board( grid1 )
    