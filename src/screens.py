from shared.MESSAGES import Messages as MESSAGE
from shared.utils import Utils as UTILS
from lib.game_board import GameBoard as GAME_BOARD
from src.gameplay import GamePlay as gameplay
from src.skynet_ai import SkynetAI as skynet
from src.attacks import Attacks as attacks
from models.coordinate_model import CoordinateModel
from models.players.player_model import PlayerModel
from models.players.player_skynet import PlayerSkynet

class Screens:
    
    coordinate_model = CoordinateModel()
    player_model = PlayerModel()
    player_skynet = PlayerSkynet()
    
    def menu():
        UTILS.clear()
        MESSAGE.DRAW_MENU()
        option_selected = MESSAGE.QUESTION_SELECTED()
        UTILS.targeting( option_selected )
        return
    
    # 1. TELA NOME DO JOGADOR ------------------------
    def screen_create_player():
        while Screens.player_model.player_name == '':
            Screens.player_model.player_name = MESSAGE.QUESTION_NAME()
            
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
        Screens.player_model.reset_player_grid()
        Screens.player_skynet.reset_skynet_grid()

        Screens.player_model.grid = gameplay.insert_ship()
        Screens.player_skynet.grid = skynet.generate_board()
        
        GAME_BOARD.generate_game_board( Screens.player_model.grid, Screens.player_skynet.grid )
        
        Screens.screen_attacks()
    
    # 4. TELA ATAQUES/TIROS --------------------------
    def screen_attacks():
        players = "A"
        
        skynetCountMoves = 0
        while players in ["A", "B"]:
            grid = None
            
            if players == "A":
                MESSAGE.LINE_HORIZONTAL()
                MESSAGE.MESSAGE_ATTACK_PLAYER( Screens.player_model.player_name )
                
                grid = Screens.player_skynet.grid
                Screens.coordinate_model = attacks.insert_attack()
                print()
            else:
                MESSAGE.LINE_HORIZONTAL()
                MESSAGE.MESSAGE_ATTACK_SKYNET()
                
                grid = Screens.player_model.grid
                Screens.coordinate_model = skynet.skynet_attack( grid, skynetCountMoves )
                skynetCountMoves += 1    
            
            players = attacks.attack( grid, Screens.coordinate_model, players )
            GAME_BOARD.generate_game_board( Screens.player_model.grid, Screens.player_skynet.grid )
            has_winner = gameplay.has_winner()
            
            if has_winner == 2:
                MESSAGE.MESSAGE_WINNER( Screens.player_model.player_name )
            elif has_winner == 1:
                MESSAGE.MESSAGE_WINNER( 'SkyNet' )
            
            if has_winner != 0:
                playagain = MESSAGE.QUESTION_PLAY_AGAIN().upper()
                while (playagain != "S") and (playagain != "N"):
                    playagain = MESSAGE.QUESTION_WARNING_COORDINATE().upper()
                if playagain == "S":
                    print( "\nComeçando uma nova partida..." )
                    skynetCountMoves = 0
                    Screens.screen_insert_ship()
                    break
                elif playagain == "N":
                    Screens.screen_exit()
                    break               


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
