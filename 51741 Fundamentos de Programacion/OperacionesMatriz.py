sitios = ["del trabajo", "de la casa", "del parque"]
ingreso = ["latitud", "longitud"]                    
latitud_sup = 2.766
latitud_inf = 2.548
longitud_or = -76.493
longitud_occ = -76.879                    
coordenadas = [[0,0],[0,0],[0,0]]

for i in range(3):
    print(f"{i + 1}. Coordenada {sitios[i]}: [Latitud =  {coordenadas[i][0]}, Longitud = {coordenadas[i][1]}]") 

if coordenadas == [[0,0],[0,0],[0,0]]:
    for i in range(3):
        for j in range(2):
            valor = float(input(f"Escriba la {ingreso[j]} {sitios[i]}: "))
            if latitud_inf <= valor <= latitud_sup or longitud_occ <= valor <= longitud_or:
                coordenadas[i][j] = valor
                continue
            else:
                print("Error coordenada")
                break                 
    for coordenada in coordenadas:
        if coordenada == 0:
            print("Error")
else:
    print("Presione 1, 2 o 3 para actualizar la reespectiva coordenadas")
    print("Presione 0 para regresar al menú")
    opcion = int(input())
    if opcion == 1:
        latitud = float(input("Ingrese la nueva latitud: "))           
        longitud = float(input("Ingrese la nueva longitud: "))
        if latitud_inf <= latitud <= latitud_sup and longitud_occ <= longitud <= longitud_or:
            coordenadas[0][0] = latitud
            coordenadas[0][1] = longitud
        else : 
            print("Error actualización")
         
    if opcion == 2:
        latitud = float(input("Ingrese la nueva latitud: "))
        longitud = float(input("Ingrese la nueva longitud: "))
        if latitud_inf <= latitud <= latitud_sup and longitud_occ <= longitud <= longitud_or:
            coordenadas[1][0] = latitud
            coordenadas[1][1] = longitud
        else : 
            print("Error actualización")

    if opcion == 3:
        latitud = float(input("Ingrese la nueva latitud: "))
        longitud = float(input("Ingrese la nueva longitud: "))
        if latitud_inf <= latitud <= latitud_sup and longitud_occ <= longitud <= longitud_or:
            coordenadas[2][0] = latitud
            coordenadas[2][1] = longitud
        else : 
            print("Error actualización")
    if opcion == 0:
        print("Buen día")

print(coordenadas)