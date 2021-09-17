from models.coordinate_model import CoordinateModel
from console.gameplay import GamePlay as game_play
import utils.CONSTANTS as CONSTANTS

class Attacks:
    
    coordinate_model = CoordinateModel()
    
    def insert_attack():
        Attacks.coordinate_model.reset()
        
        while Attacks.coordinate_model.coordinate_x < 0 or Attacks.coordinate_model.coordinate_y < 0 or Attacks.coordinate_model.coordinate_x > CONSTANTS.SIZE or Attacks.coordinate_model.coordinate_y > CONSTANTS.SIZE:
            Attacks.coordinate_model = game_play.insert_coordinate( Attacks.coordinate_model )
        
        return Attacks.coordinate_model
    
    def attack( grid, coordinate_model, player ):
        if coordinate_model.coordinate_x >= CONSTANTS.SIZE or coordinate_model.coordinate_y >= CONSTANTS.SIZE:
            return player
        
        if grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x].islower():
            return player
        
        if grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x] == " ":
            grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x] = "*"
            
            print( "Acertou a água!" )
            
            return "SKYNET" if player == "PLAYER_HUMAN" else player
        
        elif grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x].islower() or grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x] == "*":
           return player
        
        else:
            grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x] = grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x].lower()
            print( "Acertou!" )
            
            return "SKYNET" if player == "PLAYER_HUMAN" else player
    