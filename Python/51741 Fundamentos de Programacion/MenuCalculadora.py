# Imprime menú de para seleccionar la operación
print("Menú:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
seleccion = int(input(("Seleccione la operación: ")))

# Usuario ingresa valores a operar
print("Ingrese dos valores")
a = float(input("a) "))
b = float(input("b) "))

# Condicionales para transformar operación
if seleccion == 1:
    texto = "a + b = "
    operacion = a + b
elif seleccion == 2:
    texto = "a - b = "
    operacion = a - b
elif seleccion == 3:
    texto = "a * b = "
    operacion = a * b
elif seleccion == 4:
    if b != 0:
        texto = "a / b = "
        operacion = a / b
    else:
        texto = "a / b = "
        operacion = "Math ERROR" # Si división es por cero
else:
    texto = "a ^ b = "
    operacion = a ** b

# Imprime calculadora ASCII
print(" _____________________")
print("|  _________________  |")
print("| | %s %s " %(texto, operacion), end=" | |\n") # Imprime operación
print("| |_________________| |")
print("|  ___ ___ ___   ___  |")
print("| | ^ | ! | π | |AC | |")
print("| |___|___|___| |___| |")
print("|  ___ ___ ___   ___  |")
print("| | 7 | 8 | 9 | | + | |")
print("| |___|___|___| |___| |")
print("| | 4 | 5 | 6 | | - | |")
print("| |___|___|___| |___| |")
print("| | 1 | 2 | 3 | | x | |")
print("| |___|___|___| |___| |")
print("| | . | 0 | = | | / | |")
print("| |___|___|___| |___| |")
print("|_____________________|")