import time

print("Se hara un cuenta regresiva. ¿Desde que numero quieres empezar?")

valorInicial = input()

if(valorInicial.isdigit() == False):
    print("No haz puesto un numero valido")

print("Empezando cuenta regresiva... " + valorInicial)

valorInt = int(valorInicial)
tiempoInicial = time.time()

while(True):
    for x in range(0, valorInt):
        if(time.time() - tiempoInicial > 1):
            valorInt -= 1
            if(valorInt == 0):
                print("Ha acabado la cuenta regresiva")
                exit()
            elif(valorInt > 0):
                print(valorInt)
            tiempoInicial = time.time()