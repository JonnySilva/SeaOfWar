from utils.MESSAGES import Messages as MESSAGE
from utils.utils import Utils as UTILS
from console.game_board import GameBoard as GAME_BOARD
from console.gameplay import GamePlay as gameplay
from console.random_inteligency import RandomInteligency as random_inteligency
from console.attacks import Attacks as attacks
from models.coordinate_model import CoordinateModel
from models.player_model import PlayerModel
from models.player_skynet import PlayerSkynet

class Screens:
    
    coordinate_model = CoordinateModel()
    player_model = PlayerModel()
    player_skynet = PlayerSkynet()
    
    def menu():
        UTILS.clear()
        MESSAGE.DRAW_MENU()
        option_selected = MESSAGE.OPTION_SELECTED()
        UTILS.targeting( option_selected )
        return
    
    # 1. TELA NOME DO JOGADOR ------------------------
    def screen_create_player():
        while Screens.player_model.player_name == '':
            Screens.player_model.player_name = MESSAGE.DRAW_INSERT_NAME()
            
            if Screens.player_model.player_name == '':
                UTILS.clear()
                MESSAGE.MESSAGE_WARNING_EMPTY_NAME()
        else:
            Screens.screen_insert_ship()
    
    # 2. REGRAS DO JOGO ------------------------------
    def screen_game_rules():
        MESSAGE.DRAW_TITLE_GAME_RULES()
        MESSAGE.DRAW_GAME_RULES()
        MESSAGE.DRAW_BOTTON_MENU()
        option_selected = input( '\n> ' )
        UTILS.targeting( option_selected )
        return
    
    # 3. TELA INSERÇÃO DE BARCOS ---------------------
    def screen_insert_ship():
        Screens.player_model.grid = gameplay.insert_ship()
        Screens.player_skynet.grid = random_inteligency.generate_board()
        
        GAME_BOARD.generate_game_board( Screens.player_model.grid, Screens.player_skynet.grid )
        
        Screens.screen_attacks()
    
    # 4. TELA ATAQUES/TIROS --------------------------
    def screen_attacks():
        number_of_players = 0
        while number_of_players <= 1:
            if number_of_players == 0:
                print( "ataque do jogador 1!" )
                Screens.coordinate_model = attacks.insert_attack()
                number_of_players += attacks.attack( Screens.player_skynet.grid, Screens.coordinate_model )
                GAME_BOARD.generate_game_board( Screens.player_model.grid, Screens.player_skynet.grid )
            else:
                print( "ataque do jogador 2!" )
                Screens.coordinate_model = attacks.insert_attack()
                number_of_players += attacks.attack( Screens.player_model.grid, Screens.coordinate_model )
                GAME_BOARD.generate_game_board( Screens.player_model.grid, Screens.player_skynet.grid )
                
                if number_of_players == 2:
                    number_of_players = 1
    
    # 0. Sair ----------------------------------------
    def screen_exit():
        option_is_enter = MESSAGE.QUESTION_RETURN_OR_EXIT()
        UTILS.exit( option_is_enter )
    
options_menu = {
    'menu': Screens.menu,
    '1': Screens.screen_create_player,
    '2': Screens.screen_game_rules,
    '9': Screens.menu,
    '0': Screens.screen_exit
}
