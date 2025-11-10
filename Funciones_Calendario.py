from tabulate import tabulate
import LigaDeportivaAmateur
import Funciones_Calendario
import Funciones_MenuPrincipal
import datetime from datetime import timedelta


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
                listar_partidos2(LigaDeportivaAmateur.partidos)
            case 3:
                reprogramar_partido3(LigaDeportivaAmateur.partidos, LigaDeportivaAmateur.equipos)
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
            nuevopartido.update({"equipo_local": equipo["nombre"]})
    nuevoequipo_visitante = str(input(" Dime el nombre del equipo visitante"))
    for equipo in equipos:
        if nuevoequipo_visitante == equipo["nombre"]:
            nuevopartido.update({"equipo_visitante": equipo["nombre"]})
    nuevopartido.update({"ID": len(partidos) + 1, "jornada" : jornada})
    nuevahora = int(input("Dime la hora del partido:"))
    nuevopartido.update({"hora": nuevahora })
    nuevofecha = int(input("Dime la fecha del partido:"))    #Esta parafernalia es porque al hacer bool(input()) si esta lleno da true y si esta vacio da false por lo que siempre daba false porque python es mierda
    nuevopartido.update({"fecha": nuevofecha }) 
    booleano = input("Se ha jugado ya el partido? (si/no):").strip().lower()    #Esta parafernalia es porque al hacer bool(input()) si esta lleno da true y si esta vacio da false por lo que siempre daba false porque python es mierda
    nuevojugado = booleano in ["si", "sì", "s", "true", "1"]   #(Me ayudo chatGPT) es para comparar el input de usuaior a las opciones de esta lista y  asi de true o flase bien porque antes solo devolvia true
    nuevopartido.update({"jugado": nuevojugado})
    nuevoresultado = str(input("Indica el maracador (local-visitante)"))
    nuevopartido.update({"resultado":nuevoresultado})
    partidos.append(nuevopartido)
    return partidos

def listar_partidos2(partidos):
    print(tabulate(partidos)) 

def reprogramar_partido3(partidos):
    print(tabulate(partidos))
    partido_encontrado = False
    MBAPPE_MBAPPE_MBAPPE = str(input("De que ID de partido quieres cambiar la fecha/hora?"))
    for partido in partidos:
        if partido["ID"] == MBAPPE_MBAPPE_MBAPPE:
            partido_encontrado = True
            elegir2 = str(input("Quieres cambiar la fecha o la hora del partido?:")).strip().lower()
            if elegir2 == "fecha" and partido["jugado"] == False:
                Nfecha = str(input("Indica la nueva fecha del partido"))
                partido.update({"fecha":Nfecha})
                print("Fecha actualizada correctamente")
            elif elegir2 == "hora" and partido["jugado"] == False:
                Nhora = str(input("Indica la nueva hora del partido"))
                partido.update({"hora":Nhora})
            else:
                print("Por favor escoge una opcion a elegir")
        if partido_encontrado == False:
            print("Equipo no encontrado")
    return partidos

def eliminar_partido5(partidos):
    partido_encontrado = False
    print(tabulate(partidos))    
    ID_partido = str(input("¿Cual es el ID del partido a eliminar?: "))
    for partido in partidos:
        if partido["ID"] == ID_partido:
            partido_encontrado = True
            print("Partído encontrado: ", partido)
            pythonesmierda = (input("Estas seguro de que quieres borrar el partido(Acción irreversible)(si/no):")).strip().lower()
            seguro = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI DIQUE YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
            if seguro == True:
               partidos.remove(partido) 
               print("Partído eliminado correctamente")

    if partido_encontrado == False:
        print("Artículo no encontrado")
    return partidos


   

def menu_calendario_mostrado():
    print("------------------")
    print("1.Dar resultado partido")
    print("2.Listar partidos")
    print("3.Reprogramar partido")
    print("4.Eliminar partido")
    print("5.Menú principal")
    print("6.Cerrar el programa a la mierda")
    print("------------------")