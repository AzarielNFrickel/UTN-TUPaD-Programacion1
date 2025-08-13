#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima 
# por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe
# imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!!!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
residencia = input("Ingresa tu localidad de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

#Utilice import math para utilizar pi

import math

radio = float(input("Ingrese el radio del circulo: "))
area = (math.pi * radio) ** 2 
perimetro = 2 * math.pi * radio

print(f"El area del circulo es {area}, y su perimetro es de {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas
#horas equivale.

segundos = float(input("Ingrese la cantidad de segundos. "))
minutos = segundos / 60
horas = minutos / 60

print(f"La cantidad de horas es de: {horas:.3f}Hs")

#busque como redondear o mostrar menos numeros despues de la coma y esta me parecio una buena opcion (colocar : .(cantidad de decimales a mostrar)f).

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = int(input("ingrese un numero para ver su tabla de multiplicacion."))

for i in range(11): 
    resultado = num * i
    print(f"{num} * {i} = {resultado}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla 
#el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("A continuación ingrese dos números distintos de 0.")

num1 = int(input("ingrese el primer número: "))
num2 = int(input("ingrese el segundo número: ")) 

if num1 & num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    print(f"la suma es igual a: {suma}, la resta es igual a: {resta}, la multiplicacion es igual a: {multiplicacion}, y la division es igual a: {division: .3f}")
else:
    print("Los números deben ser distintos de 0.")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

print("Ingrese su altura en centimetros y su peso en Kilogramos para calcular su IMC")

altura = float(input("ingrese su altura: "))
peso = float(input("ingrese su peso: "))
    
IMC = peso / ((altura/100)**2)    

print(f"su IMC (Indice de masa corporal) es: {IMC: .4f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

print("ingrese la temperatura en celsius para convertirla a fahrenheit")

tempCelsius = float(input("ingrese la temperatura en celsius"))
tempFahrenheit = 9/5 * tempCelsius +32

print(f"La temperatura en Fahrenheit es: {tempFahrenheit: .2f} grados.")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

print("ingrese tres números para calcular su promedio. ")

num1 = int(input("ingrese el primer número"))
num2 = int(input("ingrese el segundo número"))
num3 = int(input("ingrese el tercer número"))

promedio = (num1 + num2+ num3) / 3

print(f"El promedio es de: {promedio: .2f}")