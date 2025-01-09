#Area y volumen

def area_circulo (radio):
    return(3.14*(radio**2))
    
def vol_cilindro (area_circ,alt_cil):
    return(area_circ*alt_cil)
    
radio = float(input("Ingrese el radio del circulo: "))
print("El área del circulo es",area_circulo(radio))

altura = float(input("Ingrese la altura del cilindro: "))
print("El volumen del cilindro es",vol_cilindro(area_circulo(radio),altura))