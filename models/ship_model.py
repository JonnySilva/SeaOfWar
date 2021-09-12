class AircraftCarrierModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._ship_name = "AIRCRAFT_CARRIER"
        self._ship_size = 5
    
    # Gets ---------------------------------
    @property
    def ship_name( self ):
        return self._ship_name
    
    @property
    def ship_size( self ):
        return self._ship_size

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
    