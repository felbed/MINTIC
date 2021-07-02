import math

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

user = "51741"
password = user[::-1]

a = int(user[2::])
b = int(((5*7+1)/(7-1)*5-7-1)/(1+1)-7)
resultado = a + b
print(resultado)

x = input("Ingrese su usuario:\n")

if x == user:
    y = input("Ingrese su contraseña:\n")
    if y == password:
        z = int(input("Captcha:\n%s + %s = " %(a, b)))
        if z == resultado:
            print("Sesión iniciada")
            print("Menú de opciones:")

            id = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. "]
            opcion = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana",
                    "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo",
                    "Elegir opción de menú favorita", "Cerrar sesión"]

            for i in range(len(id)):
                print(id[i] + opcion[i], sep='\n')
            seleccion = int(input(("Elija una opción: ")))

            contador = 0
            condicion = True

            while condicion:
                print("Usted ha elegido la opción %s" %(seleccion))
                if seleccion == 1:
                    actual_password = input("Ingrese su contraseña actual: ")
                    if actual_password == password:
                        new_password = input("Ingrese su nueva contraseña: ")
                        if new_password == password:
                            print("La nueva contraseña no puede ser igual a la contraseña actual")
                        else:
                            password = new_password
                    else:
                        print("Error")
                        condicion = False
                elif seleccion == 2:
                    if contador == 0:
                        coordenadas = [[0,0],[0,0],[0,0]]
                    contador += 1
                    sitios = ["del trabajo", "de la casa", "del parque"]
                    ingreso = ["latitud", "longitud"]                    
                    latitud_sup = 2.766
                    latitud_inf = 2.548
                    longitud_or = -76.493
                    longitud_occ = -76.879

                    for i in range(3):
                        print(f"{i + 1}. Coordenada {sitios[i]}: [Latitud =  {coordenadas[i][0]}, Longitud = {coordenadas[i][1]}]") 

                    if coordenadas == [[0,0],[0,0],[0,0]]:
                        for i in range(3):
                            for j in range(2):
                                valor = float(input(f"Escriba la {ingreso[j]} {sitios[i]}: "))
                                if latitud_inf <= valor <= latitud_sup or longitud_occ <= valor <= longitud_or:
                                    coordenadas[i][j] = valor
                                else:
                                    print("Error coordenada")
                                    exit()
                        seleccion = int(input(("Elija una opción: ")))
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
                                print("Hasta pronto")
                                break
                            
                        if opcion == 2:
                            latitud = float(input("Ingrese la nueva latitud: "))
                            longitud = float(input("Ingrese la nueva longitud: "))
                            if latitud_inf <= latitud <= latitud_sup and longitud_occ <= longitud <= longitud_or:
                                coordenadas[1][0] = latitud
                                coordenadas[1][1] = longitud
                            else : 
                                print("Error actualización")
                                print("Hasta pronto")
                                break

                        if opcion == 3:
                            latitud = float(input("Ingrese la nueva latitud: "))
                            longitud = float(input("Ingrese la nueva longitud: "))
                            if latitud_inf <= latitud <= latitud_sup and longitud_occ <= longitud <= longitud_or:
                                coordenadas[2][0] = latitud
                                coordenadas[2][1] = longitud
                            else : 
                                print("Error actualización")
                                print("Hasta pronto")
                                break
                        if opcion == 0:
                            print("Hasta pronto")
                        else:
                            print("Error actualización")
                            print("Hasta pronto")
                            break

                elif seleccion == 3:
                    info = [[2.698, -76.680, 63],
                            [2.724, -76.693, 20],
                            [2.606, -76.742, 680],
                            [2.698, -76.690, 15]]

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
                            condicion = False
                elif seleccion == 4:
                    condicion = False
                elif seleccion == 5:
                    condicion = False
                elif seleccion == 6:
                    seleccion = int(input("Seleccione opción favorita: "))
                    if 1 <= seleccion <= 5:
                        adivinanza1 = int(input("Para confirmar por favor responda: Soy el tercio de una docena, la respuesta correcta es "))
                        if adivinanza1 == 4:
                            adivinanza2 = int(input("Para confirmar por favor responda: Soy el menor de los enteros positivos, la respuesta correcta es "))
                            if adivinanza2 == 1:
                                opcion = [(opcion[seleccion - 1])] + [x for i,x in enumerate(opcion) if i != seleccion - 1 and i != 5 and i != 6] + opcion[5::]
                                import os
                                os.system("cls")
                                for i in range(len(id)):
                                    print(id[i] + opcion[i], sep='\n')
                                seleccion = int(input(("Elija una opción: ")))
                            else:
                                print("Error")
                                import os
                                os.system("cls")
                                for i in range(len(id)):
                                    print(id[i] + opcion[i], sep='\n')
                                seleccion = int(input(("Elija una opción: ")))
                                contador += 1
                                if contador == 3:
                                    print("Error")
                                    print("Hasta pronto")
                                    condicion = False
                        else:
                            print("Error")
                            os.system("cls")
                            for i in range(len(id)):
                                print(id[i] + opcion[i], sep='\n')
                            seleccion = int(input(("Elija una opción: ")))
                            contador += 1
                            if contador == 3:
                                print("Error")
                                print("Hasta pronto")
                                condicion = False
                    else:
                        print("Error")
                        contador += 1
                        if contador == 3:
                            print("Error")
                            print("Hasta pronto")
                            condicion = False
                elif seleccion == 7:
                    print("Hasta pronto")
                    exit()
                else:
                    print("Error")
                    contador += 1
                    if contador == 3:
                        print("Error")
                        print("Hasta pronto")
                        condicion = False
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")