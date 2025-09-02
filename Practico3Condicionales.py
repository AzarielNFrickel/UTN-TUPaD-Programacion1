#Respuestas Practico Nro 3
#1)
 
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("es mayor de edad")
else:
    print("no es mayor de edad")


#2) 

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado!")
else:
    print("Desaprobado")


#3
num= int(input("ingrese un número"))
if num%2 == 0:
    print("Ha ingresesadp un número par")
else:
    print("Por favor ingrese un número par")

#4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    categoria = "Niño"
elif edad < 18:
    categoria = "Adolescente"
elif edad < 30:
    categoria = "Adulto/a joven"
else:
    categoria = "Adulto/a"

print(f"Usted pertenece a la categoria: {categoria}")

#5

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6

import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mode, median, mean
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media == mediana == moda:
    print("No hay sesgo")
elif media > mediana:
    print("Hay sesgo positivo")
else:
    print("Hay sesgo negativo")

#7
frase = input("Ingrese una frase por favor")

len(frase)
ultimaLetra = frase[len(frase)-1]

if ultimaLetra in ["a", "e", "i", "o", "u"]:
    fraseNueva = frase + "!"
    print(fraseNueva)
else:
    print(frase)

#8
nombre= input("Ingrese su nombre")
opcion = int(input("Ingrese una opcion, 1. Nombre en mayusculas, 2. Nombre en minusculas, 3. Primera letra en mayuscula"))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Ingrese una opcion valida")


#9
magnitudTerremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitudTerremoto < 3:
    categoria = "Muy leve"
elif 3 <= magnitudTerremoto < 4:
    categoria = "Leve"
elif 4 <= magnitudTerremoto < 5:
    categoria = "Moderado"
elif 5 <= magnitudTerremoto < 6:
    categoria = "Fuerte"
elif 6 <= magnitudTerremoto < 7:
    categoria = "Muy fuerte"
else:
    categoria = "Extremo"

print(f"El terremoto se clasifica como: {categoria}")

#10
emisferio = input("Ingrese el emisferio, N para norte y S para sur: ")
emisferio = emisferio.upper()
mes= int(input("Ingrese el mes, con numeros del 1 al 12: "))
dia= int(input("Ingrese el dia: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    if emisferio == "N":
        estacion= "Invierno"
    elif emisferio == "S":
        estacion= "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if emisferio == "N":
        estacion= "Primavera"
    elif emisferio == "S":
        estacion= "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if emisferio == "N":
        estacion= "Verano"
    elif emisferio == "S":
        estacion= "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    if emisferio == "N":
        estacion= "Otoño"
    elif emisferio == "S":
        estacion= "Primavera"

print(f"Usted se encuentra en la estacion: {estacion}")
