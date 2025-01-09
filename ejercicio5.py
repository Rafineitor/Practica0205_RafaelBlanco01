#Numeros al cuadrado

def cuadrado(i):
    return(i*i)

numeros = input("Ingrese una muestra de números: ")
numeros2 = numeros.split(",")
numeros3 = [int(i) for i in numeros2]
numeros4 = []
for i in numeros3:
    c = cuadrado(i)
    numeros4.append(c)
    
print(numeros3)
print(numeros4)