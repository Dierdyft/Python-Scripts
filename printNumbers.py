things = input("Put the numbers that I will loop\nThis mode: 1-3, 4-8, 9-12\n")

if "," not in things:
    print("Not there \",\" in your input")
    exit()

things = things.split(",")
newThings = []

#Div elements contains "-"
for element in things:
    newThings.append(element.split("-"))

print("I printing your numbers")
#Analysis each element in newThings    
for element in newThings:
    #If the first numbers its highest than second number
    if int(element[0]) > int(element[1]):
            print("I cant print this numbers " + element[0] + "-" + element[1])
    #Analysis each value in range
    for i in range(int(element[0]), int(element[1]) + 1):
        if int(element[0]) == i:
            print(element[0] + "-" + element[1])
        print(i)

print("I finished my process")