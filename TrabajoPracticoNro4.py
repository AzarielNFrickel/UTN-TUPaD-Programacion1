#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("ingrese un numero entero: "))
contador = 0 
n = abs(numero) #obtenemmos el valor absoluto del numero por si ingresan un valor negativo

if n == 0:
    contador = 1
else:
    while n > 0:
        n = n // 10 #el operador // hace una division entera y elimina los decimales
        contador += 1
print(f"El numero {numero} tiene {contador} digitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

print("Ingrese dos números enteros distintos:")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
suma = 0
if num1 == num2:
    print("Debe ingresar dos números distintos.")
elif num1 < num2:
    for i in range((num1 + 1), num2, 1):
        suma += i
else:
    for i in range((num2 + 1), num1, 1):
        suma += i

print(f"La suma de los numeros comprendidos entre {num1} y {num2}, es: {suma}")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

num = int(input("A continuacion ingrese los numeros enteros que desea sumar (0 para terminar): "))
suma=0

while num!=0:
    suma += num
    num = int(input("ingrese el siguiente numero entero o 0 para terminar: "))

print(f"La suma total de los numeros ingresados es: {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numSecreto = random.randint(0, 9)
intentos = 0

numero = int(input("Adivina un el número entre 0 y 9: "))
intentos += 1
while numero != numSecreto:
    intentos += 1
    numero = int(input("Incorrecto! ingrese otro número: "))

print(f"Adivinaste! el número secreto era {numSecreto}, tuviste {intentos} intentos")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

suma=0
numero = int(input("Ingrese un número entero y positivo:"))

if numero>1:   
    for i in range(1, numero, 1):
        suma += i
elif numero == 1:
    print("No hay numeros entre 0 y 1 para sumar")
else:
    print("Debe ingresar un numero entero y positivo")

print(f"La suma de los numero comprendidos entre 0 y {numero} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contPar = 0
contImp = 0
contNeg = 0
contPos = 0
cantidadNumeros = 0


while cantidadNumeros < 100:
    num = int(input(f"Ingrese el numero {cantidadNumeros + 1}: "))
    if num % 2 == 0 or num == 0:
        contPar += 1
    else:
        contImp +=1

    if num >= 0:
        contPos += 1
    else:
        contNeg += 1

    cantidadNumeros += 1

print(f"Ingresaste {contPar} numeros pares, {contImp} impares, {contPos} positivos, {contNeg} negativos")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma=0 
cantNumeros=0

while cantNumeros < 10:
    num = int(input(f"Ingrese el numero {cantNumeros + 1}: "))
    suma += num
    cantNumeros += 1 

media = suma / cantNumeros
print(f"La media de los {cantNumeros} numeros ingresados es: {media}")
    

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero= int(input("Ingrese un numero entero positivo"))
original = numero 
inv=0


while numero > 0:
    digito = numero % 10
    inv= inv * 10 + digito
    numero = numero // 10

print(f"el numero {original} invertido es {inv}")


