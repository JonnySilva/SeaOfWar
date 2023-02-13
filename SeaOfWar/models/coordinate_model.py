class CoordinateModel( object ):
    
    def __init__( self, coordinate_x = -1, coordinate_y = -1, position = "" ):
        super().__init__()
        
        self.reset()
        self._coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y
        self._position = position
        
    def reset( self ):
        self._coordinate_x = -1
        self._coordinate_y = -1
        self._position = ""
        
    @property
    def coordinate_x( self ):
        return self._coordinate_x
        
    @coordinate_x.setter
    def coordinate_x( self, coordinate_x ):
        self._coordinate_x = coordinate_x
    
    @property
    def coordinate_y( self ):
        return self._coordinate_y
        
    @coordinate_y.setter
    def coordinate_y( self, coordinate_y ):
        self._coordinate_y = coordinate_y
    
    @property
    def position( self ):
        return self._position
        
    @position.setter
    def position( self, position ):
        self._position = position
    