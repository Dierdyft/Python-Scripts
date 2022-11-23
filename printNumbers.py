things = input("Pon los numeros a los cuales recorre por su rango\nUn ejemplo: 1-3, 4-8, 9-12\n")

things = things.split(",")
newThings = []

#Divide los elementos que contengan "-"
for element in things:
    newThings.append(element.strip().split("-"))

print("Estoy procesando los numeros")
try:
  #Recorre cada elemento de newThings    
  for element in newThings:
      #Si el primer numero es mayor que el segundo, no podra hacer el loop de estos
      if int(element[0]) > int(element[1]):
              print("No puedo mostrar este intervalo de numeros " + element[0] + "-" + element[1])
      #Recorre cada valor del elemento
      for i in range(int(element[0]), int(element[1]) + 1):
          if int(element[0]) == i:
              print(element[0] + "-" + element[1])
          print(i)

  print("He finalizado mi proceso")

except:
  print("Ha ocurrido un error durante el proceso, revisa bien tu entrada")