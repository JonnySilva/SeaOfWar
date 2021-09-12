class CruiserModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._cruiser = "CRUISER"
        self._crusier_size = 3
    
    # Gets ---------------------------
    @property
    def ship_name( self ):
        return self._cruiser
    
    @property
    def ship_size( self ):
        return self._crusier_size
    