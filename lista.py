lista=[7,9,10,7,6,7,8,10,8,9]

def promedio(lista):
    suma=0
    for i in lista:
        suma=suma+i
        return suma/len(lista)
