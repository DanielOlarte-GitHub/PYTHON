#Tipico juego de adivinar un numero entre 1 y 100 en el menor numero de intentos
import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

print("¡Bienvenido al juego de adivinanza de números!")
print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

# Inicializar el contador de intentos
intentos = 0

# Comenzar el bucle del juego
while True:
    # Pedir al usuario que ingrese un número
    numero_ingresado = int(input("Ingresa un número: "))
    intentos += 1
    
    # Comprobar si el número es el correcto
    if numero_ingresado == numero_secreto:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        break
    elif numero_ingresado < numero_secreto:
        print("El número es más alto. Intenta de nuevo.")
    else:
        print("El número es más bajo. Intenta de nuevo.")
