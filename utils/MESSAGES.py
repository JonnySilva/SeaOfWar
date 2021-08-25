class Messages:
    
    def DRAW_MENU():
        print( '''
              
                    ____        _   _   _           _     _ _____     __     __
                    |  _ \      | | | | | |         | |   (_)  __ \    \ \   / /
                    | |_) | __ _| |_| |_| | ___  ___| |__  _| |__) |____\ \_/ / 
                    |  _ < / _` | __| __| |/ _ \/ __| '_ \| |  ___/______\   /  
                    | |_) | (_| | |_| |_| |  __/\__ \ | | | | |           | |   
                    |____/ \__,_|\__|\__|_|\___||___/_| |_|_|_|           |_|   


                                         --- Bem vindo! =D ---

                                         [1]. Jogar
                                         [2]. Regras do jogo
                                         [0]. Sair
                    ************************************************************\n
        ''' )
        
    # MENSAGENS -------------------------
    def DRAW_EXIT():
        print( '''
> Tem certeza que deseja sair? (ツ)
              ''')
        
    def DRAW_EXITING():
        print( '''
> saindo''', end='' )
        
    def DRAW_SELECTED_ERROR():
        print( '''
                        ************************************************
                        * Seleção inválida, por favor tente novamente! *
                        ************************************************
                        
              ''' )
        
    # MENSAGENS DE SELEÇÃO --------------------------------------------------------
    def OPTION_SELECTED():
       return input( 'Escolha uma das opções listadas. \n> ' )
    
    def RETURN_OR_EXIT():
        return input( '''
[Enter]. Menu
[0]. Sair 

> ''' )