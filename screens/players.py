from utils import utils

class Players():
    
    def screen():
        utils.Utils.clear_screen()
        print( '=============================================================' )
        
        player_one = input( 'Digite o nome do jogador um: ' )
        player_two = input( 'Digite o nome do jogador dois: ' )
        
        players = [player_one, player_two]
        
        return players
        