from tabulate import tabulate
import LigaDeportivaAmateur
import Funciones_Calendario
import Funciones_MenuPrincipal


def menu_equipos_interno():
    opcion = 0
    while opcion != 6:
        Funciones_Calendario.menu_calendario_mostrado()
        jornada = int(input("Que número de jornada estamos?"))
        opcion = int(input("Escoge el número de la opción que desees: "))
        match opcion:
            case 1:
                crear_partido1(LigaDeportivaAmateur.equipos, LigaDeportivaAmateur.partidos, jornada)
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
        return jornada
def crear_partido1(equipos, partidos, jornada):
    nuevopartido = {}
    nuevoequipo_local = str(input(" Dime el nombre del equipo local"))
    for equipo in equipos:
        if nuevoequipo_local == equipo["nombre"]:
            nuevopartido.update()
    nuevopartido.update({"ID": len(partidos) + 1, "jornada": jornada})
    nuevoposicion = str(input("Dime su posición como jugador:")).strip().lower()
    nuevojugador.update({"posicion": nuevoposicion })
    booleano = input("Se encuentra activo en la liga? (si/no):").strip().lower()    #Esta parafernalia es porque al hacer bool(input()) si esta lleno da true y si esta vacio da false por lo que siempre daba false porque python es mierda
    nuevoactividad = booleano in ["si", "sì", "s", "true", "1"]   #(Me ayudo chatGPT) es para comparar el input de usuaior a las opciones de esta lista y  asi de true o flase bien porque antes solo devolvia true
    nuevojugador.update({"activo": nuevoactividad })
    nuevoequipo = str(input("En que equipo juega el jugador?"))
    for equipo in equipos:
        if nuevoequipo == equipo["nombre"]:
            nuevojugador.update({"nombre_equipo":nuevoequipo})
            print("Equipo asociado corectamente")
    jugadores.append(nuevojugador) 
    return jugadores
                

def menu_calendario_mostrado():
    print("------------------")
    print("1.Dar resultado partido")
    print("2.Listar partidos")
    print("3.Reprogramar partido")
    print("4.Eliminar partido")
    print("5.Menú principal")
    print("6.Cerrar el programa a la mierda")
    print("------------------")