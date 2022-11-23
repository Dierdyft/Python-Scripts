import random

print("¿Piedra, papel o tijeras?")

miEleccion = input()

#Funcion Piedra, Papel o Tijeras
def ppt(miOpcion):
    miOpcion = miOpcion.lower()

    #Opciones
    opciones = ["piedra", "papel", "tijeras"]

    if miOpcion not in opciones:
        print("Esa no es una opcion validad")
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

#While para cada vez que termine una ronda pregunte si quiere jugar nuevamente
while True:
    print("¿Quieres jugar otra vez? Escribe SI o NO")
    revancha = input()

    #Si acepta jugar
    if(revancha.lower() == "si"):
        print("¿Piedra, papel o tijeras?")
        nuevaEleccion = input()
        ppt(nuevaEleccion)
        
    #Si no quiere jugar
    elif(revancha.lower() == "no"):
        exit()
       
    #Si no resoponde nada
    else:
        print("¡Adios!")
        exit()