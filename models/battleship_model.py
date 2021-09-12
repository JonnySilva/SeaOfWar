class BattleshipModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._battleship = "BATTLESHIP"
        self._battleship_size = 4
    
    # Gets ---------------------------------
    @property
    def ship_name( self ):
        return self._battleship
    
    @property
    def ship_size( self ):
        return self._battleship_size
    