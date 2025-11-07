from tabulate import tabulate
import LigaDeportivaAmateur
import Funciones_Calendario
import Funciones_MenuPrincipal




def menu_equipos_interno():
    opcion = 0
    while opcion != 6:
        Funciones_Calendario.menu_calendario_mostrado()
        opcion = int(input("Escoge el número de la opción que desees: "))
        match opcion:
            case 1:
                print("Crear partido")
            case 2:
                print("Listar todos los partidos hechos de la liga")
            case 3:
                print("Reprogramar partido")
            case 4:
                print("Eliminar partido")
            case 5:
                Funciones_MenuPrincipal.menu_principal_interno()
            case 6:
                exit()
            case _:
                print("Lock the fuck in nigga")
                
                
def menu_calendario_mostrado():
    print("------------------")
    print("1.Dar resultado partido")
    print("2.Listar partidos")
    print("3.Reprogramar partido")
    print("4.Eliminar partido")
    print("5.Menú principal")
    print("6.Cerrar el programa a la mierda")
    print("------------------")