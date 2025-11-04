from tabulate import tabulate
import LigaDeportivaAmateur
import Funciones_Jugadores
import Funciones_MenuPrincipal

def menu_jugadores_interno():
    opcion = 0
    while opcion != 6:
        Funciones_Jugadores.menu_jugadores_mostrado()
        opcion = int(input("Escoge el número de la opción que desees: "))
        match opcion:
            case 1:
                Funciones_Jugadores.alta_jugador1(LigaDeportivaAmateur.jugadores)
            case 2:
                Funciones_Jugadores.ver_jugador2(LigaDeportivaAmateur.jugadores)
            case 3:
                Funciones_Jugadores.buscar_ID_jugador3(LigaDeportivaAmateur.jugadores)
            case 4:
                Funciones_Jugadores.actualizar_jugador4(LigaDeportivaAmateur.jugadores)
            case 5:
                Funciones_Jugadores.eliminar_jugador5(LigaDeportivaAmateur.jugadores)
            case 6:
                Funciones_MenuPrincipal.menu_principal_interno()
            case 7:
                exit()
            case _:
                print("Lock the fuck in nigga")
                
def alta_jugador1(jugadores, equipos):
    nuevojugador = {}
    nuevonombre = str(input("Dime el nombre del equipo:"))
    nuevojugador.update({"ID": len(jugadores) + 1, "nombre": nuevonombre})
    nuevoposicion = str(input("Dime su posición como jugador:")).strip().lower()
    nuevojugador.update({"precio": nuevoposicion })
    booleano = input("Se encuentran actvivos en la liga? (si/no):").strip().lower()    #Esta parafernalia es porque al hacer bool(input()) si esta lleno da true y si esta vacio da false por lo que siempre daba false porque python es mierda
    nuevoactividad = booleano in ["si", "sì", "s", "true", "1"]   #(Me ayudo chatGPT) es para comparar el input de usuaior a las opciones de esta lista y  asi de true o flase bien porque antes solo devolvia true
    nuevojugador.update({"activo": nuevoactividad })
    for equipo in equipos:
        #ME HE QUEDADO AQUI, ESTA TODo COPIADO Y PEGADO, TIENES QUE HAXCER YN FOR PARA PEDIRLE AL USUAIRO EL NOMBRE DEL EQUIPO AL QUE PERTENECE AL JUGADOR
    jugadores.append(nuevojugador) 
    return jugadores


def ver_equipos2(equipos): 
    print(tabulate(equipos))

def buscar_ID3(equipos):
    busqueda = int(input("Que ID de equipo quieres buscar?"))
    if busqueda < len(equipos) + 1:
        for equipo in equipos:
            if equipo["ID"] == busqueda:
                print(equipo)
    else:
        print("Artículo no encontrado")
        
def actualizar_equipos4(equipos):
    equipo_encontrado = False    #Esto es importante luego
    nombre_equipo = str(input("¿Cual es el nombre del equipo a actualizar?: "))
    for equipo in equipos:
        if  nombre_equipo== equipo["nombre"]:
            equipo_encontrado = True
            equipo_actualizado = equipo
            print("Equipo encontrado: ", equipo)
            print("Campos disponibles para actualizar:")
            for clave in equipos:
                if clave != "ID":
                    print(clave)
            clave = str(input("Que campo deseas actualizar?")).strip().lower()
            match clave:
                case "nombre":
                    Nnombre = str(input("Dime el nuevo nombre del equipo"))
                    equipo["nombre"] = Nnombre 
                case "precio":
                    Nciudad = float(input("Dime donde entrena el equipo ahora:"))
                    equipo["precio"] = Nciudad
                case "activo":
                    booleano = (input("Se encuentra activo el equipo?(si/no):")).strip().lower()
                    Nactivo = booleano in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
                    equipo["activo"] = Nactivo
                case _:
                    print("Opción de campo erronea")
    if equipo_encontrado == False:    #Evita posibles comportamientos extraños/bugs etc (Si lo tocas te toco)
        print("Equipo no encontrado")
    return equipo_actualizado, equipos

def eliminar_equipo5(equipos):
    equipo_encontrado = False    
    nombre_equipo = str(input("¿Cual es el nombre del equipo a eliminar?: "))
    for equipo in equipos:
        if equipo["nombre"] == nombre_equipo:
            equipo_encontrado = True
            print("Artículo encontrado: ", equipo)
            pythonesmierda = (input("Estas seguro de que quieres borrar el artículo(Acción irreversible)(si/no):")).strip().lower()
            seguro = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI DIQUE YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
            if seguro == True:
               equipos.remove(equipo) 
               print("Artículo eliminado correctamente")

    if equipo_encontrado == False:
        print("Artículo no encontrado")
    return equipos

#Funcion para mostrar el propio menu
def menu_jugadores_mostrado():
    print("------------------")
    print("1.Alta jugador")
    print("2.Listar jugadores(todos o equipos)")
    print("3.Buscar jugador por ID")
    print("4.Actualizar datos jugador")
    print("5.Eliminar jugador")
    print("6.Menu principal")
    print("7.Cerrar el programa a la verga")
    print("------------------")