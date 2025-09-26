
#1
notas = []
for i in range(10):
    entrada = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    notas.append(entrada)

print("Lista completa de notas:")
for nota in notas:
    print(nota)

suma = sum(notas)
promedio = suma / len(notas)
nota_max = max(notas)
nota_min = min(notas)

print(f"Promedio de las notas: {promedio}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

#2
productos = []
for i in range(5):
    nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
    productos.append(nombre)

productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
for prod in productos_ordenados:
    print(prod)

eliminar = input("¿Qué producto desea eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
    print("Lista actualizada:")
    for prod in productos:
        print(prod)
else:
    print(f"El producto '{eliminar}' no se encontró en la lista.")

#3
import random
numeros = []
for _ in range(15):
    numeros.append(random.randint(1, 100))

pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Cantidad de pares: {len(pares)}")
print(f"Cantidad de impares: {len(impares)}")

#4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []
for valor in datos:
    if valor not in sin_repetidos:
        sin_repetidos.append(valor)

print("Lista sin elementos repetidos:")
for elemento in sin_repetidos:
    print(elemento)


#5
estudiantes = []
for i in range(8):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    estudiantes.append(nombre)

accion = input(
    "¿Querés (A)gregar un nuevo estudiante o (E)liminar uno existente? "
).lower()

if accion == 'a':
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"Se agregó a: {nuevo}")
elif accion == 'e':
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"Se eliminó a: {eliminar}")
    else:
        print(f"El estudiante '{eliminar}' no está en la lista.")
else:
    print("Opción inválida. No se hicieron cambios.")

print("Lista final de estudiantes:")
for alumno in estudiantes:
    print(alumno)

#6
numeros = []
for i in range(7):
    num = int(input(f"Ingrese el número {i + 1} de la lista: "))
    numeros.append(num)

ultimo = numeros.pop()       
numeros.insert(0, ultimo)    

print("Lista rotada (una posición a la derecha):")
for n in numeros:
    print(n)

#7
días = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

temperaturas = []  
for i in range(7):
    temp_min = float(input(f"Ingrese la temperatura mínima de {días[i]}: "))
    temp_max = float(input(f"Ingrese la temperatura máxima de {días[i]}: "))
    temperaturas.append([temp_min, temp_max])

suma_min = 0
suma_max = 0
for temp_min, temp_max in temperaturas:
    suma_min += temp_min
    suma_max += temp_max

promedio_min = suma_min / 7
promedio_max = suma_max / 7

amplitud_máxima = 0
día_amplitud = ""
for i, (temp_min, temp_max) in enumerate(temperaturas):
    amplitud = temp_max - temp_min
    if amplitud > amplitud_máxima:
        amplitud_máxima = amplitud
        día_amplitud = días[i]


print("Promedio de temperaturas:")
print(f"Temperatura mínima promedio: {promedio_min:.2f}")
print(f"Temperatura máxima promedio: {promedio_max:.2f}")

print(f"Mayor amplitud térmica: {amplitud_máxima:.2f} °C registrada el {día_amplitud}")

#8
notas = []  
for i in range(5):
    fila = []
    for j in range(3):
        cal = float(input(f"Ingrese la nota del estudiante {i + 1}, materia {j + 1}: "))
        fila.append(cal)
    notas.append(fila)

print("Promedio de cada estudiante:")
for indice, fila in enumerate(notas, start=1):
    promedio_est = sum(fila) / len(fila)
    print(f"Estudiante {indice}: {promedio_est:.2f}")

print("Promedio de cada materia:")
for j in range(3):
    suma_mat = 0
    for i in range(5):
        suma_mat += notas[i][j]
    promedio_mat = suma_mat / 5
    print(f"Materia {j + 1}: {promedio_mat:.2f}")

#9
tablero = []
for _ in range(3):
    fila = []
    for _ in range(3):
        fila.append('-')
    tablero.append(fila)

def mostrar_tablero(tab):
    print("Tablero actual:")
    for fila in tab:
        for celda in fila:
            print(celda, end=' ')
        print()  

mostrar_tablero(tablero)
jugador = 'X'
movimientos = 0

while movimientos < 9:
    print(f"Turno de {jugador}:")
    try:
        fila = int(input("Ingrese la fila (0-2): "))
        col = int(input("Ingrese la columna (0-2): "))
    except ValueError:
        print("Entrada no válida. Debe ser un número entero entre 0 y 2.")
        continue

    if fila not in range(3) or col not in range(3):
        print("Coordenadas fuera de rango. Intente de nuevo.")
        continue
    if tablero[fila][col] != '-':
        print("Esa casilla ya está ocupada. Elija otra.")
        continue

    tablero[fila][col] = jugador
    movimientos += 1
    mostrar_tablero(tablero)

    jugador = 'O' if jugador == 'X' else 'X'

print("Fin de las 9 jugadas. ¡Gracias por jugar!")

#10
ventas = []
for i in range(4):
    fila = []
    for j in range(7):
        cantidad = float(input(f"Ingrese ventas del producto {i+1}, día {j+1}: "))
        fila.append(cantidad)
    ventas.append(fila)

totales_productos = []
print("Total vendido por producto:")
for indice, fila in enumerate(ventas, start=1):
    total = sum(fila)
    totales_productos.append(total)
    print(f"Producto {indice}: {total:.2f}")

totales_dias = []
for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
    totales_dias.append(suma_dia)

max_ventas_dia = max(totales_dias)
dia_max = totales_dias.index(max_ventas_dia) + 1
print(f"Día con mayores ventas totales: Día {dia_max} ({max_ventas_dia:.2f})")

max_ventas_prod = max(totales_productos)
prod_max = totales_productos.index(max_ventas_prod) + 1
print(f"Producto más vendido esta semana: Producto {prod_max} ({max_ventas_prod:.2f})")