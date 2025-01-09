#Media de numeros

def media(numeros):
    return(sum(numeros)/len(numeros))

numeros = input("Ingrese una muestra de números: ")
numeros2 = numeros.split(",")
numeros3 = [int(i) for i in numeros2]

print("La media de los numeros introducidos es de",media(numeros3))