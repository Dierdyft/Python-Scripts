import json, os
from datetime import datetime

#Obtener fecha actual
def dateNow():
    return datetime.now().timestamp() * 1000

#Pasar ms a HMS
def millis(value):
    millis = int(value)
    seconds = (millis/1000)%60
    seconds = int(seconds)
    minutes = (millis/(1000*60))%60
    minutes = int(minutes)
    hours = (millis/(1000*60*60))%24
    return f"{int(minutes)} minutos y {int(seconds)} segundos"
    
propiedades = { "cartera": 0, "banco": 0, "trabajar": int(dateNow()) }

fileExist = os.path.exists("./economia.json")

if(fileExist == False):
    with open("./economia.json", "w") as datos:
        json.dump(propiedades, datos)
    print("Se ha creado el archivo economia.json")
    
with open("./economia.json", "r") as datos:
    data = json.load(datos)
    trabajo = ""
    
    if int(dateNow()) >= data["trabajar"]:
            data["cartera"] += 100
            data["trabajar"] = dateNow() + 1800000
    else:
            trabajo = millis(data["trabajar"] - dateNow())
            print(f"Regresa en {trabajo}")
            exit()
    
os.remove("economia.json")
with open("./economia.json", "w") as datos:
    json.dump(data, datos, indent=4)
    
print("Haz trabajado, y ganado $100")