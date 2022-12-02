import random

letras = list("abcdefghijklmnopqrstuvwxyz")
combinacion = [""]

i = 0
while True:
  letraRandom = random.choice(letras)[0]
  if i <= 8:
    if combinacion[i-1] == letraRandom:
      combinacion.append(random.choice(letras)[0])
      i +=1
    else:
      combinacion.append(random.choice(letras)[0])
      i += 1
        
  else:
    print("".join(combinacion))
    exit()