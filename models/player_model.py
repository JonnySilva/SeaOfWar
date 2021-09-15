import utils.CONSTANTS as CONSTANTS

class PlayerModel:
    
    def __init__( self, player_name = '', grid = CONSTANTS.GRID_GAME_BOARD ):
        super().__init__()
        
        self._player_name = player_name
        self._grid = grid
    
    @property
    def player_name( self ):
        return self._player_name
    
    @player_name.setter
    def player_name( self, player_name ):
        self._player_name = player_name
    
    @property
    def grid( self ):
        return self._grid
    
    @grid.setter
    def grid( self, grid ):
        self._player_name = grid
    