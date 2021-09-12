class SubmarineAModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._submarine_a = "SUBMARINE_A"
        self._submarine_a_size = 1
    
    # Gets -------------------------------
    @property
    def ship_name( self ):
        return self._submarine_a
    
    @property
    def ship_size( self ):
        return self._submarine_a_size
    