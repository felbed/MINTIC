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
        condicion = False
    elif seleccion == 2:
        condicion = False
    elif seleccion == 3:
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
            print("Usted ha elegido la opción 3")
            condicion = False