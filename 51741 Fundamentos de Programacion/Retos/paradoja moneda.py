# NIVEL DEL DESAFÍO:
# Intermedio/Avanzado

# ENUNCIADO:
# La paradoja de la moneda consiste en un sencillo juego de probabilidades que puede generar ganancias infinitas.

# REGLAS DEL JUEGO:
# :one: Debes pagar 1.000 (mil) dólares por participar una sola vez.

# :two: En el primer turno debes lanzar la moneda; si cae cara tendrás garantizados dos dólares; si cae cruz por otro lado perderás el dinero de la participación y deberás volver a comenzar(pagando)

# :three: En los siguientes turnos; si cae cara tu dinero se verá duplicado; es decir de 2 dólares pasarás a 4 garantizados; en el siguiente turno pasarás a 8; y luego a 16; siempre de manera exponencial.

# :four: En caso de que caiga cruz, perderás el derecho a seguir participando hasta que pagues de nuevo, pero podrás llevarte todo el dinero que tenías acumulado hasta el momento.

# Como puedes notar las reglas son simples; la cosa es el participante únicamente necesita sacar cara 10 veces seguidas para que la inversión de participación se vuelva rentable y necesita únicamente 15 para obtener más de 30 mil dólares
# ¿QUÉ DEBES HACER?*
# Debes diseñar un programa que funcione bajo las reglas de la paradoja de la moneda; pero debes tener en cuenta lo siguiente.

# :one: Tengo un total de 5 mil dólares (más lo ganado durante el juego), es decir, en el peor de los casos puedo jugar 5 veces.

# :two: Dado el caso de que se logre, puedo usar el dinero ganado durante el juego para seguir participando.

# :three: Cada turno el programa deberá mostrar:
# - Este es el turno # X; si sacas cara ganarás XXXXXX dólares.

# :four: En el primer turno de cada vez que participe deberá mostrar éste mensaje:
# - Dinero total que se puede invertir -> Cuanto dinero tengo.
# - Dinero total que se ha invertido -> Cuánto dinero he gastado
# - Dinero total que he ganado en todas las rondas -> Dinero total ganado.

# :five: Siempre que se pierda; el jugador podrá elegir si quiere jugar de nuevo o no.
# MENSAJES ESPERADOS
# En el momento en que el jugador no pueda participar más por falta de dinero; o que éste decida retirarse se mostrarán los siguientes datos:

# - Usted jugó N rodas e inviritó XXXXX dólares para hacerlo.

# - El premio acumulado en sus rondas es de XXXXXXX dólares.

# - Condición a los mensajes anteriores: Usted perdió/ganó XXXXX dólares -> En el peor de los casos el jugador perderá 5 mil dólares, y la ganancia sólo se verá reflejada si el usuario al final de las rondas se queda con más de 5 mil dólares en su bolsillo.

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
