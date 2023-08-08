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
