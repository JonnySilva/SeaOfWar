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
    
    def DRAW_BOTTON_MENU():
        print( '''
[9]. Voltar
[0]. Sair
              ''' )
    
    # MENSAGENS ------------------------------------
    def MESSAGE_EXITING():
        print( '> saindo (^ – ^ *) /', end='' )
    
    def MESSAGE_RETURN_MENU():
        print( '> voltando para o menu', end='' )
    
    def MESSAGE_WARNING_EMPTY_NAME():
        print( '> Por favor, digite um nome no campo..\n' )
    
    def MESSAGE_WARNING_SHIP_OUTSIDE():
        print( '\n> A embarcação está fora do tabuleiro!' )
    
    def MESSAGE_WARNING_POSITION():
        print( '\n> Esta posição já esta ocupada!' )
    
    def MESSAGE_WARNING_CANCEL_COORDINATE():
        print( '\n> Coordenada cancelada!' )
    
    def MESSAGE_FORCE_EXIT():
        print( '\n> Saindo do jogo! \n> Bey Bey (‘▽ `) ノ' )
    
    # FIM ------------------------------------------
    
    def DRAW_SELECTED_ERROR():
        print( '''
                        ************************************************
                        * Seleção inválida, por favor tente novamente! *
                        ************************************************
                        
              ''' )
    
    def DRAW_GAME_RULES():
        print( '''
                    *******************************************************************************
                    * Batalha naval é um jogo de tabuleiro (10x10) de dois jogadores, no qual os  *
                    * jogadores têm de adivinhar em que quadrados estão os navios do oponente.    *
                    *                                                                             *
                    * Antes do início do jogo, cada jogador coloca os seus navios nos quadros,    *
                    * alinhados horizontalmente ou verticalmente.                                 *
                    *                                                                             *
                    * O número de navios permitidos é igual para ambos jogadores, os navios não   *
                    * podem se sobrepor e devem ter espaçamento de, no mínimo, um quadrado.       *
                    *                                                                             *
                    * Após os navios terem sido posicionados o jogo continua numa série de turnos.*
                    * Em cada turno, um jogador seleciona um quadrado, o qual é identificado pela *
                    * letra e número, no tauleiro do oponente, se houver um navio nesse quadrado, *
                    * é colocada uma marca vermelha, senão houver é colocada uma marca branca.    *
                    *                                                                             *
                    * Os tipos de navios são:                                                     *
                    *  # Porta-aviões (cinco quadrados)                                           *
                    *  # Encouraçado (quatro quadrados)                                           *
                    *  # Contratorpedeiros (três quadrados)                                       *
                    *  # Navio-patrulha (dois quadrados)                                          *
                    *  # Submarinos (um quadrado)                                                 *
                    *                                                                             *
                    * Vale notar que os quadrados que compõem um navio devem estar conectados     *
                    * e em fila reta.                                                             *
                    *******************************************************************************
                    * Regras retiradas do site Wikipédia, link abaixo:                            *
                    *  # https://pt.wikipedia.org/wiki/Batalha_naval_(jogo)                       *
                    *******************************************************************************
              ''' )
    
    def DRAW_TITLE_GAME_RULES():
        print( '''
                                             Regras do Jogo - Batalha Naval
                                          ------------------------------------
              ''' )
    
    # MENSAGENS DE SELEÇÃO --------------------------------------------------------
    def OPTION_SELECTED():
       return input( 'Escolha uma das opções listadas. \n> ' )
    
    def QUESTION_RETURN_OR_EXIT():
        return input( '''
> Tem certeza que deseja sair? o(〒﹏〒)o
[enter]. Menu
[0]. Sair 

> ''' )
    
    def QUESTION_HORIZONTAL_OR_VERTICAL():
        return input( '''> Deseja que o barco fique na vertical ou na horizontal?
[v]. Vertical
[h]. Horizontal

> ''' )
    
    def QUESTION_COORDINATE( ship_name, ship_size ):
        return input( f'''
Digite a coordenada que deseja colocar o {ship_name} ({ship_size} casas):
(exemplo: A1)

> ''' )
        
    def QUESTION_CONFIRMATION_COORDINATE():
        return input( '''
A coordenada está certa? (y/n)

> ''')
    
    def QUESTION_WARNING_POSITION():
        return input( "Por favor, selecione 'v' (vertical) ou 'h' (horizontal): \n> " )
    
    def DRAW_INSERT_NAME():
        return input( 'Por favor, digite o seu nome: \n> ' )
    
    # FIM -------------------------------------------------------------------------
    