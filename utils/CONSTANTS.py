from models.ship_model import AircraftCarrierModel as aircraft_carrier, BattleshipModel as battleship, CruiserModel as cruiser, PatrolShipModel as patrol_ship, SubmarineAModel as submarine_a, SubmarineBModel as submarine_b

SPACE = ' '
EMPTY = ''

# Grid ---------------------------------------
GRID_SIZE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
GRID_WIDTH = 3
SIZE = len( GRID_SIZE )

GRID_GAME_BOARD = [
    [
        SPACE for line in range( len( GRID_SIZE ) )
    ] 
    
    for column in range( len( GRID_SIZE ) )
]

temporary_grid = [
    [
        SPACE for line in range( len( GRID_SIZE ) )
    ]

    for column in range( len( GRID_SIZE ) )
]
# --------------------------------------------

# Box-drawing character ----------------------
CONST_LINE = "\u2500"                   # ─
CONST_COLUMN_LEFT = "\u251c"            # ├
CONST_COLUMN_RIGHT = "\u2524"           # ┤
CONST_COLUMN_MID = "\u253c"             # ┼
CONST_CORNER_TOP_LEFT = "\u250c"        # ┌
CONST_CORNER_TOP_RIGHT = "\u2510"       # ┐
CONST_CORNER_BOTTOM_LEFT = "\u2514"     # └
CONST_CORNER_BOTTOM_RIGHT = "\u2518"    # ┘
CONST_TOP_SEPARATOR = "\u252c"          # ┬
CONST_BOTTOM_SEPARATOR = "\u2534"       # ┴
CONST_MID_SEPARATOR = "\u2502"          # │
# --------------------------------------------

LIST_OF_SHIP_MODELS = [
    
    aircraft_carrier(),
    battleship(),
    cruiser(),
    patrol_ship(),
    submarine_a(),
    submarine_b()
    
]
