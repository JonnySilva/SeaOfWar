import random

import utils.CONSTANTS as CONSTANTS
from models.coordinate_model import CoordinateModel
from console.gameplay import GamePlay as gameplay

class RandomInteligency:
    
    coordinate_model = CoordinateModel()
    
    def generate_board():
        for ship_model in CONSTANTS.LIST_OF_SHIP_MODELS:
            RandomInteligency.random_insertion( CONSTANTS.GRID_IA, ship_model )
            
        return CONSTANTS.GRID_IA
            
    def random_insertion( grid, ship_model ):
        inserted = False
        RandomInteligency.coordinate_model.reset()
        
        while not inserted:
            RandomInteligency.coordinate_model.coordinate_x = random.randint( 0, 9 )
            RandomInteligency.coordinate_model.coordinate_y = random.randint( 0, 9 )
            RandomInteligency.coordinate_model.position = random.randint( 0, 1 )
            
            if RandomInteligency.coordinate_model.position == 0:
                RandomInteligency.coordinate_model.position = "V"
            else:
                RandomInteligency.coordinate_model.position = "H"
            
            inserted = gameplay.position_ship( grid, ship_model, RandomInteligency.coordinate_model, False)
        