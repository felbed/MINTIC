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
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")

