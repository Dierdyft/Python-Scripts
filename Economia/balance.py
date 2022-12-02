import json, os
from datetime import datetime

#Obtener fecha actual
def dateNow():
    return datetime.now().timestamp() * 1000
    
#Pasar ms a HMS
def millis(value):
    millis = int(value)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24
    return f"{int(minutes)} minutos y {int(seconds)} segundos"

fileExist = os.path.exists("./economia.json")

propiedades = { "cartera": 0, "banco": 0, "trabajar": int(dateNow()) }

if(fileExist == False):
    with open("./economia.json", "w") as datos:
        json.dump(propiedades, datos)
        print("Se ha creado el archivo economia.json")

else:
    with open("./economia.json", "r") as datos:
        data = json.load(datos)
        cartera = data["cartera"]
        banco = data["banco"]
        trabajo = []
        if int(dateNow()) >= data["trabajar"]:
            trabajo = "Ya puedes trabajar"
        else:
            trabajo = millis(data["trabajar"] - dateNow())
    
        print(f"Cartera: {cartera}\nBanco: {banco}\nTrabajo: Dentro de {trabajo}")