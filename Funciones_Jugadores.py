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
                Funciones_Jugadores.alta_jugador1(LigaDeportivaAmateur.jugadores, LigaDeportivaAmateur.equipos)
            case 2:
                Funciones_Jugadores.ver_jugador2(LigaDeportivaAmateur.jugadores)
            case 3:
                Funciones_Jugadores.buscar_ID_jugador3(LigaDeportivaAmateur.jugadores)
            case 4:
                Funciones_Jugadores.actualizar_jugador4(LigaDeportivaAmateur.jugadores, LigaDeportivaAmateur.equipos)
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
    nuevonombre = str(input("Dime el nombre del jugador:"))
    nuevojugador.update({"ID": len(jugadores) + 1, "nombre": nuevonombre})
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


def ver_jugador2(jugadores): 
    print("------------------")
    print("1.De toda la liga")
    print("2.De un equipo")
    print("------------------")
    eleccion = int(input("Quieres listar todos los jugadores de la liga o los de un equipo en particular?"))
    if eleccion == 1:
        print(tabulate(jugadores))  
    elif eleccion == 2:
        jugadoresxequipo = []   #Se crea una nueva lista para guardar todo los jugadores del equipo seleccionado
        cualequipo = str(input("De que equipo quieres buscar sus jugadores?"))
        for jugador in jugadores:
            if jugador["nombre_equipo"] == cualequipo:
                jugadoresxequipo.append(jugador)
        print(tabulate(jugadoresxequipo))
    else:
        print("Equipo no encontrado")
        
def buscar_ID_jugador3(jugadores):
    busqueda = int(input("Que ID de jugador quieres buscar?"))
    if busqueda < len(jugadores) + 1:
        for jugador in jugadores:
            if jugador["ID"] == busqueda:
                print(jugador)
    else:
        print("Jugador no encontrado")
        
def actualizar_jugador4(jugadores, equipos):
    jugador_encontrado = False    #Esto es importante luego
    nombre_jugador = str(input("¿Cual es el nombre del jugador a actualizar?: "))
    for jugador in jugadores:
        if  nombre_jugador == jugador["nombre"]:
            jugador_encontrado = True
            jugador_actualizado = jugador
            print("Jugador encontrado: ", jugador)
            print("Campos disponibles para actualizar:")
            for clave in jugador:
                if clave != "ID":
                    print(clave)
            clave = str(input("Que campo deseas actualizar?")).strip().lower()
            match clave:
                case "nombre":
                    Nnombre = str(input("Dime el nuevo nombre del jugador"))
                    jugador["nombre"] = Nnombre 
                case "posicion":
                    Nposicion = float(input("Dime la nueva posición del jugador:"))
                    jugador["posicion"] = Nposicion
                case "equipo_id":
                    equipo_encontrado = False
                    Nequipo = str(input("Dime el nombre del equipo al que se traspasa el jugador"))
                    for equipo in equipos:
                        if equipo["nombre"] == Nequipo:
                            equipo_encontrado = True 
                            jugador["id_equipo"] = equipo["ID"]
                            print("Equipo asociado correctamente")
                    if equipo_encontrado == False:
                        print("Equipo no encontrado") 
                case "activo":
                    booleano = (input("Se encuentra activo el jugador?(si/no):")).strip().lower()
                    Nactivo = booleano in ["si", "sí", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
                    jugador["activo"] = Nactivo
                case _:
                    print("Opción de campo erronea")
    if jugador_encontrado == False:    #Evita posibles comportamientos extraños/bugs etc (Si lo tocas te toco)
        print("Jugador no encontrado")
    return jugador_actualizado, jugadores

def eliminar_jugador5(jugadores):
    jugador_encontrado = False    
    nombre_equipo = str(input("¿Cual es el nombre del jugador a eliminar?: "))
    for jugador in jugadores:
        if jugador["nombre"] == nombre_equipo:
            jugador_encontrado = True
            print("Jugador encontrado: ", jugador)
            pythonesmierda = (input("Estas seguro de que quieres borrar el jugador?(Acción irreversible)(si/no):")).strip().lower()
            seguro = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI DIQUE YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
            if seguro == True:
               jugadores.remove(jugador) 
               print("Jugador eliminado correctamente")

    if jugador_encontrado == False:
        print("Artículo no encontrado")
    return jugadores

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