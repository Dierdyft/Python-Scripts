#Librerias necesarias
from blessed import Terminal
term = Terminal()
import os

#Variables necesarias
words = []

#Funcion del juego
def game(word, lives):
    
    print(f"Intenta adivinar la palabra. La palabra tiene {len(word)} letras")
    
    attempts = 0
    
    while attempts < lives:
        wordUser = input()
        os.system("clear")

        correctWord = word
        correctWord = list(correctWord)

        if len(wordUser) > len(correctWord):
            print(f"No es posible jugar con una palabra de mas de {len(correctWord)} letras")
            return
    
        wordUser = list(wordUser)
    
        i = 0
        
        if "".join(correctWord) == "".join(wordUser):
            print("Haz acertado en la palabra!")
            return

        for x in wordUser:
            if x in correctWord:
                if x == correctWord[i]:
                    wordUser[i] = term.green + x
                else:
                    wordUser[i] = term.yellow + x
            else:
                wordUser[i] = term.grey + x
            i += 1

        words.append(wordUser)

        attempts += 1
        
        print(f"Intentos restantes: {attempts}")

        for x in words:
            print("".join(x))
            
    else:
        print("No tienes vidas :'v")
        return
              
#Iniciar el juego
game("iglesia", 5)