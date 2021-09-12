class PatrolShipModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._patrol_ship = "PATROL_SHIP"
        self._patrol_ship_size = 2
    
    # Gets ----------------------------
    @property
    def ship_name( self ):
        return self._patrol_ship
    
    @property
    def ship_size( self ):
        return self._patrol_ship_size
    