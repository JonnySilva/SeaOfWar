class PatrolShipModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._ship_name = "Barco Patrulha"
        self._ship_code = "PATROL_SHIP"
        self._ship_size = 2
    
    # Gets ----------------------------
    @property
    def ship_name( self ):
        return self._ship_name
    
    @property
    def ship_code( self ):
        return self._ship_code
    
    @property
    def ship_size( self ):
        return self._ship_size
    