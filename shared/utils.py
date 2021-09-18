import os
import sys
import numpy as np
from time import sleep
from shared.MESSAGES import Messages as MESSAGE
import src.screens as screen

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
            
        Utils.draw_points()
        
    def draw_points():
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
            MESSAGE.MESSAGE_INVALID_SELECTED()
            Utils.return_menu()
        else:
            try:
                screen.options_menu[option]()
            except KeyError:
                MESSAGE.MESSAGE_INVALID_SELECTED()
                Utils.return_menu()
    
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
        
    def coordinate_is_digit( coordinate ):
        return coordinate.isdigit()

    def convert_grid_to_skynet_solution(grid):
        gridArray = np.asarray(grid)
        desired_array1 = np.asarray([[j.replace(' ', '0') for j in i] for i in gridArray])
        desired_array2 = np.asarray([[j.replace('S', '1') for j in i] for i in desired_array1])
        desired_array3 = np.asarray([[j.replace('M', '1') for j in i] for i in desired_array2])
        desired_array4 = np.asarray([[j.replace('B', '1') for j in i] for i in desired_array3])
        desired_array5 = np.asarray([[j.replace('G', '1') for j in i] for i in desired_array4])
        desired_array6 = np.asarray([[j.replace('T', '1') for j in i] for i in desired_array5])
        desired_array = np.asarray([[j.replace('R', '1') for j in i] for i in desired_array6])
        
        desired_arrayInt = desired_array.astype(np.int)

        return desired_arrayInt
    