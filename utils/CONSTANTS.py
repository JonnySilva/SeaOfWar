from models.aircraft_carrier_model import AircraftCarrierModel as aircraft_carrier
from models.battleship_model import BattleshipModel as battleship
from models.crusier_model import CruiserModel as cruiser
from models.patrol_ship_model import PatrolShipModel as patrol_ship
from models.submarina_a_model import SubmarineAModel as submarine_a
from models.submarine_b_model import SubmarineBModel as submarine_b

SPACE = ' '
EMPTY = ''

# Grid ---------------------------------------
GRID_SIZE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
GRID_WIDTH = 3
SIZE = len( GRID_SIZE )

GRID_GAME_BOARD = [
    [
        SPACE for coordinate_y in range( len( GRID_SIZE ) )
    ]
    
    for coordinate_x in range( len( GRID_SIZE ) )
]

GRID_IA = [
    [
        SPACE for coordinate_y in range( len( GRID_SIZE ) )
    ]
    
    for coordinate_x in range( len( GRID_SIZE ) )
]

PUBLIC_GRID = [
    [
        SPACE for coordinate_y in range( len( GRID_SIZE ) )
    ]
    
    for coordinate_x in range( len( GRID_SIZE ) )
]

temporary_grid = [
    [
        SPACE for coordinate_y in range( len( GRID_SIZE ) )
    ]

    for coordinate_x in range( len( GRID_SIZE ) )
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

# List of Ship Models ----------------------
LIST_OF_SHIP_MODELS = [
    
    aircraft_carrier(),
    battleship(),
    cruiser(),
    patrol_ship(),
    submarine_a(),
    submarine_b()
    
]
# --------------------------------------------

# Constants used in Skynet Class -------------
CONST_SEQUENCE = 'Sequence'
CONST_CHROMOSSOME = 'Chromosome'
CONST_GENERATION = 'Generation'
CONST_BIRTH = 'Birth'
CONST_FITNESS = 'Fitness'
CONST_PARENTS = 'Parents'
CONST_ELITE = 'Elite'
CONST_ELITISM = 'Elitism'
CONST_RANDOM = 'Random'
CONST_MUTATION = 'Mutation'
CONST_SPLICE_PAIR = 'Splice Pair'
# --------------------------------------------
