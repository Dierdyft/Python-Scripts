def cuadrado(num1, num2):
    
    if num1.isdigit() == False:
        print("La longitud X no es un numero")
        return
    
    if num2.isdigit() == False:
        print("La longitud Y no es un numero")
        return    
        
    filas = ["□"] #■
    filas *= int(num1)
    filas.append("\n")
    
    filasJoin = "".join(filas)
    filasJoin *= int(num2)
    print(filasJoin)

#Aplicando la funcion
inpud1 = input("Ingresa la longitud X del cuadrado ")
inpud2 = input("Ingresa la longitud Y del cuadrado ")

try: 
    cuadrado(inpud1, inpud2)
except:
    print("Ha ocurrido un error inesperado")