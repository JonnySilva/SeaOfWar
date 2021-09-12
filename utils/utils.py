import os
import sys
from time import sleep
from utils.MESSAGES import Messages as MESSAGE
import console.screens as screen
from models.ship_model import AircraftCarrierModel as aircraft_carrier, BattleshipModel as battleship, CruiserModel as cruiser, PatrolShipModel as patrol_ship, SubmarineAModel as submarine_a, SubmarineBModel as submarine_b

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
            MESSAGE.MESSAGE_EXITING()
        elif exit_or_loading == 1:
            MESSAGE.MESSAGE_RETURN_MENU()
            
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
                
    
    def ship_names_enum( ship_name ):
        return {
            
            aircraft_carrier().ship_name: "Porta-Aviões",
            battleship().ship_name: "Encouraçado",
            cruiser().ship_name: "Cruzador",
            patrol_ship().ship_name: "Barco Patrulha",
            submarine_a().ship_name: "Submarino",
            submarine_b().ship_name: "Submarino"
            
        }[ship_name]
        
    def letter_to_column_number( letter ):
        return {
            
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
            "I": 8,
            "J": 9
            
        }[letter.upper()]
        