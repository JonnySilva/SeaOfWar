class CruiserModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._ship_name = "Cruzador Bahia"
        self._ship_code = "BAHIA"
        self._ship_size = 3
    
    # Gets ---------------------------
    @property
    def ship_name( self ):
        return self._ship_name
    
    @property
    def ship_code( self ):
        return self._ship_code
    
    @property
    def ship_size( self ):
        return self._ship_size
    