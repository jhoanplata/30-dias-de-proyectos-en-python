import random

# Genera un numero aleatorio entre 1 y 100
numero = random.randint(1, 100)

print("Adivina un numero entre 1 y 100")

# Recibe un numero del usuario
numero_usuario = int(input("Ingrese un numero: "))


while numero!= numero_usuario:
    if numero < numero_usuario:
        print("El numero es menor")
        numero_usuario = int(input("Ingrese un numero: "))
    elif numero > numero_usuario:
        print("El numero es mayor")
        numero_usuario= int(input("Ingrese un numero: "))
    else:
        break

print("Felicidades, adivinaste el numero")

