import random

# Definir una lista de palabras para el juego
palabras = ['gato', 'perro', 'elefante', 'jirafa', 'leon', 'tigre', 'oso', 'cacatua', 'cerdo']

# Elegir una palabra al azar de la lista
palabra_secreta = random.choice(palabras)

# Definir las variables para el juego
vidas = 8
letras_adivinadas = []

# Función para mostrar el estado actual del juego
def mostrar_juego():
    print("\nPalabra secreta:", end=" ")
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\nVidas restantes:", vidas, "\n")

# Mostrar el estado inicial del juego
mostrar_juego()

# Bucle principal del juego
while True:
    # Pedir al usuario que ingrese una letra
    letra = input("Ingrese una letra: ")
    
    # Comprobar si la letra ya fue adivinada
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra. Intenta otra.")
    # Comprobar si la letra está en la palabra secreta
    elif letra in palabra_secreta:
        print("¡Adivinaste una letra!")
        letras_adivinadas.append(letra)
        # Comprobar si el usuario adivinó todas las letras
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡Felicidades! Adivinaste la palabra secreta:", palabra_secreta)
            break
    # Si la letra no está en la palabra secreta
    else:
        print("La letra no está en la palabra secreta. Pierdes una vida.")
        vidas -= 1
        # Comprobar si el usuario se quedó sin vidas
        if vidas == 0:
            print("¡Oh no! Te quedaste sin vidas. La palabra secreta era:", palabra_secreta)
            break
    
    # Mostrar el estado actual del juego
    mostrar_juego()
