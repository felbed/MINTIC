lista = [1,2,3,4,5]

print(lista)

print(lista[::-1])

n = int(input("Ingrese el tamaño del arreglo: "))

lista = []

for i in range(n):
    valor = float(input("Ingrese un dato: "))
    lista.append(valor)

print(lista[::-1])