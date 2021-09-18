import shared.CONSTANTS as CONSTANTS

class Messages:
    
    def DRAW_LINE( amout ):
        return CONSTANTS.CONST_LINE * amout
    
    def LINE_HORIZONTAL():
        txt = "-"
        x = txt.center( 100, "-" )
        
        print( x )
    
    # MENU ----------------------------------------
    def DRAW_MENU():
        LINE = Messages.DRAW_LINE( 51 )

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
                             {CONSTANTS.CONST_CORNER_BOTTOM_LEFT}{LINE}{CONSTANTS.CONST_CORNER_BOTTOM_RIGHT}''' )
    
    # SCREEN GAME RULES ----------------------------------------
    def DRAW_GAME_RULES():
        LINE = Messages.DRAW_LINE( 79 )
        
        print( f'''
                    {CONSTANTS.CONST_CORNER_TOP_LEFT}{LINE}{CONSTANTS.CONST_CORNER_TOP_RIGHT}
                    {CONSTANTS.CONST_MID_SEPARATOR}  Batalha naval é um jogo de tabuleiro (10x10) de dois jogadores, no qual os   {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  jogadores têm de adivinhar em que quadrados estão os navios do oponente.     {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}                                                                               {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  Antes do início do jogo, cada jogador coloca os seus navios nos quadros,     {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  alinhados horizontalmente ou verticalmente.                                  {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}                                                                               {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  O número de navios permitidos é igual para ambos jogadores, os navios não    {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  podem se sobrepor e devem ter espaçamento de, no mínimo, um quadrado.        {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}                                                                               {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  Após os navios terem sido posicionados o jogo continua numa série de turnos. {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  Em cada turno, um jogador seleciona um quadrado, o qual é identificado pela  {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  letra e número, no tauleiro do oponente, se houver um navio nesse quadrado,  {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  é colocada uma marca vermelha, senão houver é colocada uma marca branca.     {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}                                                                               {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  Os tipos de navios são:                                                      {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}   # Porta-aviões (cinco quadrados)                                            {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}   # Encouraçado (quatro quadrados)                                            {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}   # Contratorpedeiros (três quadrados)                                        {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}   # Navio-patrulha (dois quadrados)                                           {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}   # Submarinos (um quadrado)                                                  {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}                                                                               {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  Vale notar que os quadrados que compõem um navio devem estar conectados      {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}  e em fila reta.                                                              {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_COLUMN_LEFT}{LINE}{CONSTANTS.CONST_COLUMN_RIGHT}
                    {CONSTANTS.CONST_MID_SEPARATOR}  Regras retiradas do site Wikipédia, link abaixo:                             {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_MID_SEPARATOR}   # https://pt.wikipedia.org/wiki/Batalha_naval_(jogo)                        {CONSTANTS.CONST_MID_SEPARATOR}
                    {CONSTANTS.CONST_CORNER_BOTTOM_LEFT}{LINE}{CONSTANTS.CONST_CORNER_BOTTOM_RIGHT}''' )
    
    def DRAW_TITLE_GAME_RULES():
        LINE = Messages.DRAW_LINE( 36 )
        
        print( f'''
                                              Regras do Jogo - Batalha Naval
                                          {CONSTANTS.CONST_CORNER_BOTTOM_LEFT}{LINE}{CONSTANTS.CONST_CORNER_BOTTOM_RIGHT}''' )
    
    def DRAW_BOTTON_MENU():
        print( '\n[9]. Voltar\n[0]. Sair' )
    
    # MESSAGES ----------------------------------------
    def MESSAGE_EXITING():
        print( '\n> Saindo (^ – ^ *) /', end=CONSTANTS.EMPTY )
    
    def MESSAGE_FORCE_EXIT():
        print( '\n> Saindo do jogo! \n> Bey Bey (‘▽ `) ノ' )
    
    def MESSAGE_RETURN_MENU():
        print( '\n> Voltando para o menu', end=CONSTANTS.EMPTY )
    
    def MESSAGE_WARNING_EMPTY_NAME():
        print( '\n> Nenhum nome inserido no campo..' )
    
    def MESSAGE_WARNING_SHIP_OUTSIDE():
        print( '\n> \033[1;31mA embarcação não pode ficar fora do tabuleiro!\033[0m\n' )
    
    def MESSAGE_WARNING_POSITION():
        print( '\n> \033[1;31mEsta posição já esta ocupada!\033[0m\n' )
    
    def MESSAGE_WARNING_CANCEL_COORDINATE():
        print( '\n> \033[1;31mCoordenada cancelada!\033[0m\n' )
    
    def MESSAGE_SKYNET_THINKING():
        print( f'\n> SkyNet:\n  — Estou criando uma estratégia e irei te ganhar', end=CONSTANTS.EMPTY )
    
    def MESSAGE_ATTACK_PLAYER( player_name='' ):
        print( f'\n> Esta é a vez do(a) \33[33m{player_name}\033[0m!' )
    
    def MESSAGE_ATTACK_SKYNET():
        print( '\n> Esta é a vez da \33[33mSkyNet\033[0m!' )
    
    def MESSAGE_WINNER( player_name='' ):
        if player_name == 'SkyNet':
            print( '\n> SkyNet:\n  — Eu avisei que ganharia! ¯\_(ツ)_/¯' )
        else:
            print( f'\n\033[92mO(A) {player_name} ganhou!\033[0m' )
    
    def MESSAGE_HIT_WATTER():
        print( '\n> \033[94mAcertou a água!\033[0m \n')
    
    def MESSAGE_HIT_SHIP():
        print( '\n> \033[92mAcertou um barco!\033[0m \n' )
    
    def MESSAGE_INVALID_SELECTED():
        LINE = Messages.DRAW_LINE( 60 )
        print( f'''
                        {CONSTANTS.CONST_CORNER_TOP_LEFT}{LINE}{CONSTANTS.CONST_CORNER_TOP_RIGHT}
                          \033[1;91mSeleção inválida, por favor selecione uma opção existente!\033[0m
                        {CONSTANTS.CONST_CORNER_BOTTOM_LEFT}{LINE}{CONSTANTS.CONST_CORNER_BOTTOM_RIGHT}''' )
    
    # QUESTIONS ----------------------------------------
    def QUESTION_SELECTED():
       return input( '\nEscolha uma das opções listadas acima. \n> ' )
    
    def QUESTION_RETURN_OR_EXIT():
        return input( '\nTem certeza que deseja sair? o(〒﹏〒)o\n\n[ENTER]. Menu\n[0]. Sair \n> ' )
    
    def QUESTION_HORIZONTAL_OR_VERTICAL():
        return input( '\nDeseja que o barco fique na vertical ou na horizontal?\n[V]. Vertical\n[H]. Horizontal\n> ' )
    
    def QUESTION_COORDINATE( ship_name, ship_size ):
        return input( f'\nDigite a coordenada que deseja colocar o {ship_name} ({ship_size} casas):\n(exemplo: A1)\n> ' )
    
    def QUESTION_ATTACK():
        return input( '\nQual a coordenada do ataque?\n> ' )
    
    def QUESTION_CONFIRMATION_COORDINATE():
        return input( '\nA coordenada está certa? (S/N)\n> ' )
    
    def QUESTION_WARNING_COORDINATE():
        return input( "\nPor favor, seleciona 'S' (sim) ou 'N' (não): \n> " )
    
    def QUESTION_WARNING_POSITION():
        return input( "\nPor favor, selecione 'V' (vertical) ou 'H' (horizontal):\n> " )
    
    def QUESTION_NAME():
        return input( '\nDigite o seu nome:\n> ' )
    
    def QUESTION_PLAY_AGAIN():
        return input( '\nGostaria de Jogar novamente? (S/N)\n> ' )
    