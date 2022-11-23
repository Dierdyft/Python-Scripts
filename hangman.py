import random

palabras = ["ciudad", "palacio", "urbanizacion", "festival"]

espaciosPalabra = []
vidas = 5
palabra = random.choices(palabras)[0]
palabraSeparada = list(palabra)

#print(palabraSeparada) ←Muestra la palabra completa

#Determinar los espacios de la palabra
for x in palabra:
    espaciosPalabra.append("_")

#Inicio
print("Vamos a jugar al ahorcado")
print(" ".join(espaciosPalabra))
print("Vidas:", vidas)

print("Dame una letra, si no pertenece a la palabra perderas una vida")

#Inicio del juego.k
while True:
    letra = input()

    #Funcion Principal
    def  info():
        indeX = 0
        for m in palabraSeparada:
            if m in letra:
                espaciosPalabra[indeX] = letra
            indeX += 1
        print(" ".join(espaciosPalabra))
        print("Vidas:", vidas)
        if(" ".join(espaciosPalabra) == " ".join(palabraSeparada)):
            print("¡Haz ganado, felicidades!")
            exit()
    
    #Si tiene vidas
    if(vidas > 1):
        #No le ha dado la letra antes
        if(letra not in espaciosPalabra):
            #Si la letra esta
            if(letra in palabraSeparada):
                print("¡La letra pertenece a la palabra!")
                info()
            #Si la letra NO esta
            elif(letra not in palabraSeparada):
                print("¡La letra NO pertenece a la palabra!")
                vidas -= 1
                info()
        
        #Ya le habidado esa letra
        else:
            print("¡Ya me haz dado esa letra con anterioridad!")
            info()
        
    #Si NO tiene vidas
    else:
        print("Ya no tienes vidas, perdiste")
        exit()