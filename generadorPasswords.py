#Generador de contraseñas
import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

longitud = int(input("Ingrese la longitud de la contraseña: "))
contraseña_generada = generar_contraseña(longitud)
print("Contraseña generada:", contraseña_generada)
