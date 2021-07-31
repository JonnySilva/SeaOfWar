lines = 10
columns = 10

space = ' '
empty = ''

class GameBoard():

    def print_game_board():
        print( f'\n{space * 3}', end=empty )
        for position_column in range( 0, columns ):
            number_of_column = str( position_column )
            print( number_of_column + (space * 2), end=empty )
        
        print( '' )

        for position_line in range( 0, lines ): 
            number_of_line = str( position_line ) + ':'
            print( number_of_line, space + '*  ' * columns )
