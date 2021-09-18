import shared.CONSTANTS as CONSTANTS

class PlayerModel:
    
    def __init__( self, player_name = '', grid = CONSTANTS.GRID_GAME_BOARD ):
        super().__init__()
        
        self._player_name = player_name
        self._grid = grid

    def reset_player_grid( self ):
        CONSTANTS.GRID_GAME_BOARD = [
            [
                CONSTANTS.SPACE for coordinate_y in range( len( CONSTANTS.GRID_SIZE ) )
            ]
            
            for coordinate_x in range( len( CONSTANTS.GRID_SIZE ) )
        ]
        self._grid = CONSTANTS.GRID_GAME_BOARD 

    
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
        self._grid = grid
    