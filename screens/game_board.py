class GameBoard():
    
    def print_game_board(players):
        columns = 10
        lines = 10

        space = ' '
        empty = ''
        
        print( '\n     ', end=empty )
        for i in range( 0, columns ):
            print( str( i ) + '  ', end=empty )

        print( '' )
        for i in range( 0, lines ):
            print( str( i ) + ':', '  *' * columns, ' |' )
