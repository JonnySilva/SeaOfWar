import string

SPACE = ' '
EMPTY = ''

# Grid ---------------------------------------
GRID_SIZE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
GRID_WIDTH = 3

GRID_GAME_BOARD = [
    [
        SPACE for line in range( len( GRID_SIZE ) )
    ] 
    
    for column in range( len( GRID_SIZE ) )
]
# --------------------------------------------

# Box-drawing character ----------------------
CONST_LINE = "\u2500"                   # ─
CONST_COLUMN_LEFT = "\u251c"            # ├
CONST_COLUMN_RIGHT = "\u2524"           # ┤
CONST_COLUMN_MID = "\u253c"             # ┼
CONST_CORNER_TOP_LEFT = "\u250c"        # ┌
CONST_CORNER_TOP_RIGHT = "\u2510"       # ┐
CONST_CORNER_BOTTOM_LEFT = "\u2514"     # └
CONST_CORNER_BOTTOM_RIGHT = "\u2518"    # ┘
CONST_TOP_SEPARATOR = "\u252c"          # ┬
CONST_BOTTOM_SEPARATOR = "\u2534"       # ┴
CONST_MID_SEPARATOR = "\u2502"          # │
# --------------------------------------------

class GameBoard:
    
    def generate_space( amount, final ):
        print( f'{SPACE * int( amount )}', end=final )
    
    def draw_line():
        print( f'{CONST_LINE * int( GRID_WIDTH )}', end=EMPTY )
    
    def draw_line_top( spaces=0 ):
        GameBoard.generate_space( spaces, EMPTY )
        print( CONST_CORNER_TOP_LEFT, end=EMPTY )
        
        for square_top in range( len( GRID_SIZE ) ):
            GameBoard.draw_line()
            print( CONST_CORNER_TOP_RIGHT if square_top == 9 else CONST_TOP_SEPARATOR, end=EMPTY )
    
    def draw_line_mid( spaces=0 ):
        GameBoard.generate_space( spaces, EMPTY )
        print( CONST_COLUMN_LEFT, end=EMPTY )
        
        for square_mid in range( len( GRID_SIZE ) ):
            GameBoard.draw_line()
            print( CONST_COLUMN_RIGHT if square_mid == 9 else CONST_COLUMN_MID, end=EMPTY )
    
    def draw_line_bottom( spaces=0 ):
        GameBoard.generate_space( spaces, EMPTY )
        print( CONST_CORNER_BOTTOM_LEFT, end=EMPTY )
        
        for square_bottom in range( len( GRID_SIZE ) ):
            GameBoard.draw_line()
            print( CONST_CORNER_BOTTOM_RIGHT if square_bottom == 9 else CONST_BOTTOM_SEPARATOR, end=EMPTY )
    
    def draw_game_board( grid=None ):
        # grid = grid if grid == None else GRID_GAME_BOARD
        
        if grid == None:
            grid = GRID_GAME_BOARD
        
        for column in range( len( grid ) ):
            if column == 0:
                GameBoard.generate_space( 2, EMPTY )
            
            GameBoard.generate_space( 2, EMPTY )
            print( string.ascii_uppercase[column], end=EMPTY ) # printing letters/columns (A-J) in the terminal..
            GameBoard.generate_space( 1, EMPTY )
        
        print()
        GameBoard.draw_line_top( 2 )
        print()
        
        for line in range( len( grid ) ):
            print( line, end=SPACE )
            
            for width in range( len( grid ) ):
                print( CONST_MID_SEPARATOR, end=EMPTY )
                print( f'{SPACE}{grid[line][width]}{SPACE}', end=EMPTY )
                
            print( CONST_MID_SEPARATOR )
            
            if line != 9:
                GameBoard.draw_line_mid( 2 )
                print()
        
        GameBoard.draw_line_bottom( 2 )
        print()
    