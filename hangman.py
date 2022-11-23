import random
import os

palabras = ["ciudad", "palacio", "urbanizacion", "festival", "zapato", "colegio", "tomillotiempillo"]

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

#Inicio del juego
while True:
    letra = input()

    #Funcion Principal
    def info():
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
    if(vidas > 0):
        #Si "letra" es igual a la palabra
        if(letra == palabra):
            print("¡Haz ganado, felicidades!")
            exit()
        else:
            #No le ha dado la letra antes
            if(letra not in espaciosPalabra):
                #Si la letra esta
                if letra in palabraSeparada:
                    os.system("clear")
                    print("La letra pertenece a la palabra")
                    info()
                #Si la letra NO esta
                elif(letra not in palabraSeparada):
                    print("La letra NO pertenece a la palabra")
                    vidas -= 1
                    print("Vidas: " + str(vidas))
            #Ya le habidado esa letra
            else:
                if(letra == "_"):
                    print("Esa letra no es valida")
                else:
                    os.system("clear")
                    print("Ya me haz dado esa letra con anterioridad")
                    info()
        #Si NO tiene vidas
    else:
        print("¡Ya no tienes vidas, perdiste!")
        exit()