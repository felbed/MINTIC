import math

info = [[2.698, -76.680, 63],
        [2.724, -76.693, 20],
        [2.606, -76.742, 680],
        [2.698, -76.690, 15]]

sitios = ["del trabajo", "de la casa", "del parque"]
ingreso = ["latitud", "longitud"]  

latitud_sup = 2.766
latitud_inf = 2.548
longitud_or = -76.493
longitud_occ = -76.879

def distancia(latitud, longitud):
    R = 6372.795477598
    distancias = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(12):
        latitud1 = info[i][0]
        longitud1 = info[i][1]
        usuarios = info[i][2]
        delta_lat = latitud1 - latitud
        delta_lon = longitud1 - longitud
        distancias[i][0] = 2 * R * math.asin(math.sqrt((math.sin(delta_lat/2)**2)+(math.cos(latitud)*math.cos(latitud1))*(math.sin(delta_lon/2)**2)))
        distancias[i][1] = usuarios
    return sorted(distancias, key = lambda x: x[1])

for i in range(4):
    latitud = info[i][0]
    longitud = info[i][1]
    if latitud_inf <= latitud <= latitud_sup and longitud_occ <= longitud <= longitud_or:
        continue
    else:
        print("Error coordenada")
        break

if contador == 0:
    print("Error sin registro de coordenadas")
else:
    for i in range(3):
        print(f"{i + 1}. Coordenada {sitios[i]}: [Latitud =  {coordenadas[i][0]}, Longitud = {coordenadas[i][1]}]")

    opcion = int(input("Por favor elija su ubicación actual(1,2 ó 3)para calcular ladistancia a los puntos de conexión"))

    if opcion == 1:
        print("Zonas wifi cercanas con menos usuarios")
        dist = distancia(latitud=coordenadas[opcion - 1][0], longitud=coordenadas[opcion - 1][1])
        for i in range(2):
            print(f"La zona wifi {i + 1}: ubicada a {dist[i][0]} metros, tiene en promedio {dist[i][1]} usuarios") 
        print("Elija 1 o 2 para recibir indicaciones de llegada")
    if opcion == 2:
        print("Zonas wifi cercanas con menos usuarios")
        dist = distancia(latitud=coordenadas[opcion - 1][0], longitud=coordenadas[opcion - 1][1])
        for i in range(2):
            print(f"La zona wifi {i + 1}: ubicada a {dist[i][0]} metros, tiene en promedio {dist[i][1]} usuarios") 
        print("Elija 1 o 2 para recibir indicaciones de llegada")
    if opcion == 3:
        print("Zonas wifi cercanas con menos usuarios")
        dist = distancia(latitud=coordenadas[opcion - 1][0], longitud=coordenadas[opcion - 1][1])
        for i in range(2):
            print(f"La zona wifi {i + 1}: ubicada a {dist[i][0]} metros, tiene en promedio {dist[i][1]} usuarios") 
        print("Elija 1 o 2 para recibir indicaciones de llegada")
    else:
        print("Error ubicación")

