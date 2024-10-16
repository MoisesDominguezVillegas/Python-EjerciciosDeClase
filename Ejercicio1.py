# PRIMER EJERCICIO
nombre = input("Escribe tu nombre aqui: ")
print(f"Hola {nombre}! Me alegro de conocerle")

# SEGUNDO EJERCICIO
nombre = input("Escribe tu nombre aqui: ")
nombre_mayuscula = nombre.upper()
print (nombre_mayuscula)

caracteres = len(nombre)
print (f"El nombre {nombre} tiene {caracteres} caracteres")

for i in range(caracteres):
    print(nombre)
    
# TERCER EJERCICIO
numero_maximo = int(input("Escribe un numero maximo: "))

if numero_maximo >= 2:
    for numero in range (numero_maximo):
        if numero %2 == 0:
            print (numero +2)
        
# CUARTO EJERCICIO
peso = int(input("Escriba su peso en Kg: "))
altura = int(input("Escriba su altura en cm: "))

imc = round(peso / (altura / 100) ** 2 ,2)

print (f"Tu indice de masa corporal es {imc}")

# QUINTO EJERCICIO
import random

numero_azar1 = random.randint(2, 10)
numero_azar2 = random.randint(2, 10)

numero = numero_azar1 * numero_azar2
numero_usuario = int(input("Escriba un numero: "))

if numero_usuario == numero:
    print ("Felicidades, has acertado!")
else:
    print ("Lo siento, no has acertado.")
    print (f"El numero seleccionado era {numero}")


