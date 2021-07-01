# NIVEL DEL DESAFÍO:
# Principiante

# ENUNCIADO:
# Alpha Centauri es la segunda estrella más cercana a nuestro planeta; está aproximadamente a 4.36 años luz de distancia. 
# Los científicos necesitan saber a cuantos kilómetros equivale dicha distancia; 
# y adicionalmente desean saber cuántos años tardaría la nave más rápida que conocemos la "Sonda Solar Parker" la cual viaja 430.000 millas por horas en llegar hasta la estrella.
# 1: La velocidad de la luz es: 299.792,458 kilómetros por segundo.
# 2: Una milla por hora equivale a 1.60934 kilómetros por hora

alpha_centauri = 4.36 # Años luz de distancia

al = 299792.458*(60)*(60)*(24)*(365) # Un año luz kilómetros/año

distancia = al * alpha_centauri

print(f"La distancia a Alpha Centauri son {distancia} kilómetros.")

velocidad_ssp = 430000 # millas/hora

velocidad_ssp *= 1.60934 # kilómetros/hora

velocidad_ssp = velocidad_ssp*(24)*(365) # Velocidad Sonda Solar Parker kilometros/año

tiempo = distancia / velocidad_ssp

print(f"La Sonda Solar Parker tardaría {tiempo} años en llegar a Alpha Centauri viajando a 430.000 millas por hora.")