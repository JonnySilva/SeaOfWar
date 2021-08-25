from utils.MESSAGES import Messages as MESSAGE
from utils.utils import Utils as UTILS

class Screens:
    
    def menu():
        UTILS.clear()
        MESSAGE.DRAW_MENU()
        option_selected = MESSAGE.OPTION_SELECTED()
        UTILS.targeting( option_selected )
        return
    
    # 0. Sair ----------------------------------------
    def screen_exit():
        MESSAGE.DRAW_EXIT()
        option_is_enter = MESSAGE.RETURN_OR_EXIT()
        UTILS.exit( option_is_enter )
    
options_menu = {
    'menu': Screens.menu,
    '0': Screens.screen_exit
}