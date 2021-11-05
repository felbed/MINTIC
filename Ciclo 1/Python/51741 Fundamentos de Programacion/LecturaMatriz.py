matriz = [[1,2],[3,4]]

print(matriz)

n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))

matrix = [[float(input("Escriba la entrada: ")) for j in range(m)] for i in range(n)]

print(matrix)


# For printing the matrix 
for i in range(n):
    for j in range(m): 
        print(f"{matrix[i][j]}", end =" ") 
    print() 