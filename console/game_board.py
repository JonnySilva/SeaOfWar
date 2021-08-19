import console

columns = 10
lines = 10
empty = ''

class GameBoard:
    
    def draw_game_board():
        
        players = 1
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        
        print( 'IMPRIMINDO TABULEIROS'.ljust(50))
        
        while( players <= 2 ):    
            print( '    ', end=empty )
            for column in range( 0, columns ):
                print( str( column ) + '   ', end=empty )
                
            print( '' )
            
            for letter in range(0, len( alphabet ) ):
                print( str( alphabet[letter] ) + ':', ' █  ' * columns, '' )
                
            if players == 1:
                print( ' - ' * 14 )
            players += players
            