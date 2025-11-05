#Funcion que activa el bucle del menu principal
def menu_principal_interno():
    import Funciones_MenuPrincipal
    import Funciones_Equipos
    import Funciones_Jugadores
    import Funciones_Calendario
    import Funciones_Clasificacion
    opcion = 0
    while opcion != 4:
        Funciones_MenuPrincipal.menu_principal_mostrado()
        opcion = int(input("Escoge el número de la opción que desees: "))
        match opcion:
            case 1:
                Funciones_Equipos.menu_equipos_interno()
            case 2:
                Funciones_Jugadores.menu_jugadores_interno()
            case 3:
                print("Menu Calendario")
            case 4:
                print("Menu clasificación")
            case 5:
                exit()
            case _:
                print("Lock the fuck in nigga")
                
                
#Funcion que activa el mostrar el menu principal (Se hace todo desde la otra funcion)             
def menu_principal_mostrado():
    print("------------------")
    print("1.Menu equipo")
    print("2.Menu jugadores")
    print("3.Menu calendario")
    print("4.Menu clasificacion")
    print("5.Cerrar el programa a la verga")
    print("------------------")