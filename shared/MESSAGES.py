import shared.CONSTANTS as CONSTANTS

class Messages:
    
    def DRAW_MENU():
        LINE = CONSTANTS.CONST_LINE * 51
        
        print( f'''
              
 \033[1;34m     ___           ___           ___      \033[0m\033[1;33m     ___           ___    \033[0m\033[1;31m     ___           ___           ___      \033[0m
 \033[1;34m    /  /\         /  /\         /  /\     \033[0m\033[1;33m    /  /\         /  /\   \033[0m\033[1;31m    /__/\         /  /\         /  /\     \033[0m
 \033[1;34m   /  /:/_       /  /:/_       /  /::\    \033[0m\033[1;33m   /  /::\       /  /:/_  \033[0m\033[1;31m   _\_ \:\       /  /::\       /  /::\    \033[0m
 \033[1;34m  /  /:/ /\     /  /:/ /\     /  /:/\:\   \033[0m\033[1;33m  /  /:/\:\     /  /:/ /\ \033[0m\033[1;31m  /__/\ \:\     /  /:/\:\     /  /:/\:\   \033[0m
 \033[1;34m /  /:/ /::\   /  /:/ /:/_   /  /:/~/::\  \033[0m\033[1;33m /  /:/  \:\   /  /:/ /:/ \033[0m\033[1;31m _\_ \:\ \:\   /  /:/~/::\   /  /:/~/:/   \033[0m
 \033[1;34m/__/:/ /:/\:\ /__/:/ /:/ /\ /__/:/ /:/\:\ \033[0m\033[1;33m/__/:/ \__\:\ /__/:/ /:/  \033[0m\033[1;31m/__/\ \:\ \:\ /__/:/ /:/\:\ /__/:/ /:/___ \033[0m
 \033[1;34m\  \:\/:/~/:/ \  \:\/:/ /:/ \  \:\/:/__\/ \033[0m\033[1;33m\  \:\ /  /:/ \  \:\/:/   \033[0m\033[1;31m\  \:\ \:\/:/ \  \:\/:/__\/ \  \:\/:::::/ \033[0m
 \033[1;34m \  \::/ /:/   \  \::/ /:/   \  \::/      \033[0m\033[1;33m \  \:\  /:/   \  \::/    \033[0m\033[1;31m \  \:\ \::/   \  \::/       \  \::/~~~~  \033[0m
 \033[1;34m  \__\/ /:/     \  \:\/:/     \  \:\      \033[0m\033[1;33m  \  \:\/:/     \  \:\    \033[0m\033[1;31m  \  \:\/:/     \  \:\        \  \:\      \033[0m
 \033[1;34m    /__/:/       \  \::/       \  \:\     \033[0m\033[1;33m   \  \::/       \  \:\   \033[0m\033[1;31m   \  \::/       \  \:\        \  \:\     \033[0m
 \033[1;34m    \__\/         \__\/         \__\/     \033[0m\033[1;33m    \__\/         \__\/   \033[0m\033[1;31m    \__\/         \__\/         \__\/     \033[0m

                             {CONSTANTS.CONST_CORNER_TOP_LEFT}{LINE}{CONSTANTS.CONST_CORNER_TOP_RIGHT}
                                              --- Bem vindo! =D ---

                                               [1]. Jogar
                                               [2]. Regras do jogo
                                               [0]. Sair
                             {CONSTANTS.CONST_CORNER_BOTTOM_LEFT}{LINE}{CONSTANTS.CONST_CORNER_BOTTOM_RIGHT}
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
        
    def LINE_HORIZONTAL():
        txt = "-"
        x = txt.center(100, "-")
        print(x)
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
       return input( 'Escolha uma das opções listadas acima. \n> ' )
    
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
    
    def QUESTION_ATTACK():
        return input( '''Qual a coordenada do ataque?
> ''' )
    
    def QUESTION_CONFIRMATION_COORDINATE():
        return input( '''
A coordenada está certa? (s/n)
> ''')
    
    def QUESTION_WARNING_COORDINATE():
        return input( "Por favor, seleciona 's' (sim) ou 'n' (não): \n> " )
    
    def QUESTION_WARNING_POSITION():
        return input( "Por favor, selecione 'v' (vertical) ou 'h' (horizontal): \n> " )
    
    def DRAW_INSERT_NAME():
        return input( 'Por favor, digite o seu nome: \n> ' )

    def QUESTION_PLAY_AGAIN():
        return input( "\n> Gostaria de Jogar novamente? (s/n)" )
    
    # FIM -------------------------------------------------------------------------
    