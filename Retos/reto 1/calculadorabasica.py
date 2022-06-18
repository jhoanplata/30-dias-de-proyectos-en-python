def saludo(nombre):
    print("Bienvenido " + nombre)

nombre_usuario = input("¡Hola! , ¿Cómo te llamas? ")
saludo(nombre_usuario)

nunber1=int (input("Ingrese un número: "))
nunber2=int (input("Ingrese otro número:"))

elección = 0

while elección != 6:
    print ("""
    Indique la operación a realizar:
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Cambio de valores
    6) Salir
    """)

    elección = int(input("Ingrese una opción: "))
    if  elección == 1:
        print("La suma de los números es: ", nunber1 + nunber2)
    elif elección == 2:
        print("La resta de los números es: ", nunber1 - nunber2)
    elif elección == 3:
        print("La multiplicación de los números es: ", nunber1 * nunber2)
    elif elección == 4:
        print("La división de los números es: ", nunber1 / nunber2)
    elif elección == 5:
        nunber1=int (input("Ingrese un número: "))
        nunber2=int (input("Ingrese otro número:"))
    elif elección == 6:
        print("Gracias por usar el programa " + nombre_usuario , "¡Hasta pronto! \n")
    else:
        print("Ingrese una opción válida")

    switch = int(input("¿Desea continuar? (1) Si (2) No: "))
    if switch == 1:
        continue
    