#Numero a factorial

def fact_rec(a):
    if a<0:
        print("Error.")
    if a==0:
        return(1)
    if a >= 1:
        return a * fact_rec(a - 1)
        
def fact_int(a):
    for i in range(a,1,-1):
        c = a*(a-1)
        return c

entero = int(input("Ingrese un numero entero positivo: "))
print(fact_rec(entero))
print(fact_int(entero))