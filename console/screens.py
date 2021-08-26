from utils.MESSAGES import Messages as MESSAGE
from utils.utils import Utils as UTILS

class Screens:
    
    def menu():
        UTILS.clear()
        MESSAGE.DRAW_MENU()
        option_selected = MESSAGE.OPTION_SELECTED()
        UTILS.targeting( option_selected )
        return
    
    # 2. REGRAS DO JOGO ------------------------------
    def screen_game_rules():
        MESSAGE.DRAW_TITLE_GAME_RULES()
        MESSAGE.DRAW_GAME_RULES()
        MESSAGE.DRAW_BOTTON_MENU()
        option_selected = input( '\n> ' )
        UTILS.targeting( option_selected )
        return
    
    # 0. Sair ----------------------------------------
    def screen_exit():
        option_is_enter = MESSAGE.QUESTION_RETURN_OR_EXIT()
        UTILS.exit( option_is_enter )
    
options_menu = {
    'menu': Screens.menu,
    '2': Screens.screen_game_rules,
    '9': Screens.menu,
    '0': Screens.screen_exit
}