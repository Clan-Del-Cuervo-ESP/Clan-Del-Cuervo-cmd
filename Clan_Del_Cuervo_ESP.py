import time

def print_logo():
    print("""
    .             .     .                           
    |             |     |                           
,-. | ,-: ;-.   ,-| ,-. |   ,-. . . ,-. ;-. . , ,-. 
|   | | | | |   | | |-' |   |   | | |-' |   |/  | | 
`-' ' `-` ' '   `-' `-' '   `-' `-` `-' '   '   `-'
""")

def print_menu():
    print("""
 ______________________________ 
|  __________________________  |
| | sitios donde estamos [1] | |
| | acerqua del clan     [2] | |
| | Niveles              [3] | |
| | cuantos somos        [4] | |
| | Salir                [5] | |
| |__________________________| |
|______________________________|
""")

def option1():
    print("Cargando módulo 1... Espere por favor...")

    time.sleep(3)

    print("\nC:\Clan Del Cuervo\sitios donde estamos")

    print("""
      _____________________________________________________________  
    ||-Youtube:https://www.youtube.com/@CLAN_DEL_CUERVO            ||
    ||                                                             ||
    ||-Instagram:https://www.instagram.com/clan_del_cuervo_logrono_||
    ||                                                             ||
    ||-TikTok:https://www.tiktok.com/@clan_del_cuervo_             ||
    ||                                                             ||
    ||-https://github.com/Clan-Del-Cuervo-ESP                      ||
    ||_____________________________________________________________||""")
    

def option3():
    print("Cargando módulo 3... Espere por favor...")

    print("\n C:\Clan Del Cuervo\ Niveles ")


    time.sleep(3)

    print("""
    +----------------+------------------+-------------+
    | Altos cargos   |Cargos intermedios|Cargos bajos |
    +----------------+------------------+-------------+
    | Jefe           | Paladin          | Iniciado    |
    | Vicepresidente | Caballero        |             |
    | Primer ministro|                  |             |
    +----------------+------------------+-------------+
    """)
    
def option2():

    print("Cargando módulo 2... Espere por favor...")

    print("\nC:\Clan Del Cuervo\ acerca del clan")


    time.sleep(3)

    print("""                                              
                                                            *
                                                             *
              _________________                               *
    __________|Acerca del clan|_____________________________|*|____
    ||*+**+*+*+*+*+*+**+*+*+**+*+*+*+*+*+*+*+*+*+*+*+**+*+*+*+*+*+/
    ||-Somos un grupo que ayuda a gente                         | |
    ||                                                          | |
    ||-No somos muchos por ahora, pero en un futuro seremos más | |
    ||                                                          | |
    ||-Contacto: clandelcuervolgn@gmail.com                     | |
    ||________________________________________España____________|_|
    ||                                                            |
    \\____________________________________________________________/""") 

def option4():

    print("Cargando módulo 4... Espere por favor...")

    print("\nC:\Clan Del Cuervo\cuantos somos")


    time.sleep(3)

    print("""
    +---------------+      
    |¿CUÁNTOS SOMOS?|
    +---------------+------------+
    |EN INSTAGRAM            [28]|
    |EN TIKTOK               [4] |
    |EN YOUTUBE              [9] |
    |EN GITHUB               [0] |
    +------------------+---------+
    |Por favor síguenos|
    +------------------+
    """)

def option5():
    time.sleep(2) 
    print("Saliendo...")

    exit()

def main():

    while True:
        
        print_logo()
        print_menu()

        
        try:
            choice = int(input("\nC:\Clan Del cuervo> "))

            if choice == 1:
                option1()

            elif choice == 2:
                option2()

            elif choice == 3:
                option3()

            elif choice == 4:
                option4() 

            elif choice == 5:
                option5()

            else:
                
                print('Ingrese un número válido porfavor .')

        except ValueError:

            print('Ingrese un número válido.')

if __name__ == '__main__':

    main()
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XX                                                                          XX
# XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
# XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
# XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
# XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
# XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
# XX   MMMMMy''                                                    ''yMMMMM   XX
# XX   MMMy'                                                          'yMMM   XX
# XX   Mh'                                                              'hM   XX
# XX   -                                                                  -   XX
# XX                                                                          XX
# XX   ::                                                                ::   XX
# XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
# XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
# XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
# XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
# XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
# XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
# XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
# XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
# XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
# XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
# XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
# XX                                oo      oo                                XX
# XX           oM                 oo          oo                 Mo           XX
# XX         oMMo                M              M                oMMo         XX
# XX       +MMMM                 s              s                 MMMM+       XX
# XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
# XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
# XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
# XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
# XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
# XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
# XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
# XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
# XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
# XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
# XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
# XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
# XX   MMMMMMMM-                                                  -MMMMMMMM   XX
# XX   MMMMMMMMM                                                  MMMMMMMMM   XX
# XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
# XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
# XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
# XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
# XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
# XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
# XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
# XX                                                                          XX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#     .o88o.                               o8o                .
#     888 `"                               `"'              .o8
#    o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
#     888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
#     888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
#     888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
#    o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8
