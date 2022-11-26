#Inicio funcion principal
def bar(total, progress, length, charEmpty, charFill):
    
    if total.isdigit() == False:
        print("No es un numero valido")
        return
    
    if progress.isdigit() == False:
        print("No es un numero valido")
        return
        
    if length.isdigit() == False:
        print("No es un numero valido")
        return
    else:
        if int(length) <= 0:
            print("La longitud de la barra debe ser mayor a 0")
    
    if int(progress) > int(total):
        print("El progreso no puede ser mayor al total")
        return
        
    if len(charEmpty) > 1:
        print("No es un caracter valido")
        return
    
    if len(charFill) > 1:
        print("No es un caracter valido")
        return
    
    total = int(total)
    progress = int(progress)
    percentage = int((progress / total) * 100)
    
    barLength = int(length)
    barProgress = []
    
    #Añade el caracter vacio segun el numero de espacios
    for i in range(0, barLength):
        barProgress.append(charEmpty)
    
    #Reemplazando el charEmpty por el charFill (Llenando la barra)
    value = int((progress / total) * barLength)
    for barIndex in range(0, value):
        barProgress[barIndex] = charFill
       
    #Imprime la barra de progreso
    print("".join(barProgress))
        
#Inputs/Entradas
totalUse = input("Escribe el total de la barra de progreso: ")

progressUse = input("Escribe el progreso de la barra de progreso: ")

lengthUse = input("Escribe la longitud de la barra de progreso: ")
    
emptyUse = input("Escribe el caracter de vacio de la barra de progreso: ")
    
fillUse = input("Escribe el caracter de relleno de la barra de progreso: ")

#Usando funcion
try:
    bar(totalUse, progressUse, lengthUse, emptyUse, fillUse)
except:
    print("Ha ocurrido un error inesperado")

#Simbolos que uso: □ & ■