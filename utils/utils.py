import os
import sys
from time import sleep
from utils.MESSAGES import Messages as MESSAGE
import console.screens as screen

class Utils:
    
    def clear():
        os.system( 'cls' if os.name == 'nt' else 'clear' )
    
    def exit( option_is_enter ):
        if option_is_enter == '':
            Utils.return_menu()
        else:
            try:
                sys.exit()
            except SystemExit:
                Utils.clear()
                Utils.loading_or_exit( 0 )
    
    def loading_or_exit( exit_or_loading = 0 ):
        if exit_or_loading == 0:
            MESSAGE.DRAW_EXITING()
        elif exit_or_loading == 1:
            MESSAGE.DRAW_RETURN_MENU()
            
        secconds = 0
        
        while secconds < 3:
            sleep( 1 )
            print( '.', end='' )
            secconds += 1
        print( '\n' )
    
    def return_menu():
        Utils.loading_or_exit( 1 )
        screen.options_menu['menu']()
        
    def targeting( option_selected ):
        Utils.clear()
        
        option = option_selected.lower()
        
        if option == '':
            MESSAGE.DRAW_SELECTED_ERROR()
            Utils.return_menu()
        else:
            try:
                screen.options_menu[option]()
            except KeyError:
                MESSAGE.DRAW_SELECTED_ERROR()
                Utils.return_menu()