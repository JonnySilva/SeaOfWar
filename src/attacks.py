from models.coordinate_model import CoordinateModel
from src.gameplay import GamePlay as game_play
import shared.CONSTANTS as CONSTANTS
from shared.MESSAGES import Messages as MESSAGE

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
            grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x] = "\033[94mX\033[0m"
            
            MESSAGE.MESSAGE_HIT_WATTER()
            MESSAGE.LINE_HORIZONTAL()
            
            if player == "A":
                player = "B"
                return player
            else:
                player = "A"
                return player
        
        elif grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x].islower() or grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x] == "\033[94mX\033[0m":
           return player
        
        else:
            grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x] = grid[coordinate_model.coordinate_y][coordinate_model.coordinate_x].lower()
            
            MESSAGE.MESSAGE_HIT_SHIP()
            MESSAGE.LINE_HORIZONTAL()
            
            if player == "A":
                player = "B"
                return player
            else:
                player = "A"
                return player
    