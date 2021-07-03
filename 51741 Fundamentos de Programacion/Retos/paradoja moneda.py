import random # Módulo para aleatorizar

total = 5000 # Dinero inicial
participacion = 1000 # Inversión por participación
# Contadores
turno = 0
ganado = 0
perdido = 0
N = 0

# Bucle: corre el juego hasta donde el jugador indique
while total >= participacion:
    N += 1
    turno += 1
    if turno == 1:
        print(f"- Dinero total que se puede invertir -> {total}.")
        print(f"- Dinero total que se ha invertido -> {perdido}")
        print(f"- Dinero total que he ganado en todas las rondas -> {ganado}.")
    print(f"Este es el turno #{turno}; si sacas cara ganarás {2**turno} dólares.")
    lanzamiento = random.choice(["C", "S"]) # Lanzamiento de moneda
    if lanzamiento == "C":
        ganado += 2**turno # Ganancia
        total += ganado
    else:
        perdido += participacion 
        total -= participacion # Perdida
        turno = 0
        repite = input("¿Quiere jugar de nuevo? S/n: ")
        if repite == "S" or repite == "s":
            if total < participacion:
                print(f"- Usted jugó {N} rodas e inviritió {perdido} dólares para hacerlo.")
                print(f"- El premio acumulado en sus rondas es de {total} dólares.")
                break
            else:
                continue
        if repite == "N" or repite == "n":
            break
