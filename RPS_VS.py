print("¡Jugaran piedra, papel o tijeras!")

opciones = ["piedra", "papel", "tijeras"]

print("JUGADOR 1 haga su eleccion")
jugadorUno = input()
#metodo para borrar el mensaje
if jugadorUno.lower() not in opciones:
    print("JUGADOR 1 esa no es una opcion valida")
    exit()
    
print("JUGADOR 2 haga su eleccion")
jugadorDos = input()
#metodo para borrar el mensaje
if jugadorDos.lower() not in opciones:
    print("JUGADOR 2 esa no es una opcion valida")
    exit()
    
def ppt(jugadorUno, jugadorDos):
    opcionUno = jugadorUno.lower()
    opcionDos = jugadorDos.lower()

    #Opciones
    opciones = ["piedra", "papel", "tijeras"]

    if opcionUno not in opciones:
        print("JUGADOR 1 esa no es una opcion validad")
        exit()
    if opcionDos not in opciones:
        print("JUGADOR 2 esa no es una opcion validad")
        exit()        
    
    #Eleccion del bot
    opcionBot = random.choice(opciones)
    print("El bot ha elegido " + opcionBot)

    #Si el bot elige piedra
    if(opcionBot == "piedra"):
        if(miOpcion == "papel"):
            print("¡Haz ganado!")
        elif(miOpcion == "tijeras"):
            print("Haz perdido")
        elif(miOpcion == opcionBot):
            print("Ha ocurrido un empate")
        
    #Si el bot elige papel
    elif(opcionBot == "papel"):
        if(miOpcion == "tijeras"):
            print("¡Haz ganado!")
        if(miOpcion == "piedra"):
            print("Haz perdido")
        elif(miOpcion == opcionBot):
            print("Ha ocurrido un empate")
        
    #Si el bot elige tijeras
    elif(opcionBot == "tijeras"):
        if(miOpcion == "piedra"):
            print("¡Haz ganado!")
        if(miOpcion == "papel"):
            print("Haz perdido")
        elif(miOpcion == opcionBot):
            print("Ha ocurrido un empate")
        
ppt(miEleccion)
