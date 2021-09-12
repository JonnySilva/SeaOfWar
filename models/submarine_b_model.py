class SubmarineBModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._submarine_b = "SUBMARINE_B"
        self._submarine_b_size = 1
    
    # Gets ------------------------------
    @property
    def ship_name( self ):
        return self._submarine_b
    
    @property
    def ship_size( self ):
        return self._submarine_b_size
    