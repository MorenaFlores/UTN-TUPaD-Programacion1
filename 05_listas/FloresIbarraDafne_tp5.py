# EJERCICIO 1
notas = [10, 9, 8, 6, 5, 9, 7, 6, 10, 5]

#Mostrar la lista
print("Notas de 10 estudiantes:")
for i in notas:
    print(f"Nota: {i}")
print("---------------------------------")

# Calcular y mostrar promedio:
sumatoria = 0
for i in notas:
    sumatoria += i
promedio = sumatoria/len(notas)


#Nota más alta y baja:
nota_alta = notas[0]
nota_baja = notas[0]

for i in notas:
    if i>nota_alta:
        nota_alta=i
    elif i<nota_baja:
        nota_baja=i

#Mostrar resultados
print(f"La nota más alta es: {nota_alta}")
print("---------------------------------")
print(f"La nota más baja es: {nota_baja}")
print("---------------------------------")
print(f"El promedio de las notas es: {promedio}")
print("---------------------------------")

print("//////////////////////////////////////////////////////////////////////////////////////////////")

#EJERCICIO 2
lista = []

#Pedir 5 productos al usuario
for i in range(5):
    productos = input(f"Ingrese el producto {i+1}:")
    lista.append(productos) #Agregar a la lista

#Mostrar la lista alfabeticamente
lista_ordenada = sorted(lista)
print(lista_ordenada)

#Productos a eliminar:
producto_eliminado = input("Ingrese el producto que desea eliminar: ")
lista.remove(producto_eliminado)
#Actualizar la lista
print(sorted(lista))

print("//////////////////////////////////////////////////////////////////////////////////////////////")

#EJEERCICIO 3:
#Importar 15 números al azar
import random
numeros_aleatorios = [random.randint(1,100) for j in range (15)]

pares = []
impares = []

#Identificar pares e impares
for i in numeros_aleatorios:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

#Mostrar resultados
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

print("//////////////////////////////////////////////////////////////////////////////////////////////")

# EJERCICIO 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_ordenada = []

#Crear nueva lista sin elementos repetidos

for i in range (len(datos)):
    if datos[i] not in datos_ordenada:
        numero = datos[i]
        datos_ordenada.append(numero)

#Mostrar resultado
print(f"Lista original: {datos}")
print(f"Lista sin repetidos: {datos_ordenada}")

#EJERCICIO 5
estudiantes = ["Dafne", "Morena", "Yael", "Tomas", "Cristian", "Joaquin", "Selene", "Dylan"]

valor = True

while valor:
    print("----------------------------------------------------------------------")
    print(f"Lista actualizada: {estudiantes}")
    print("----------------------------------------------------------------------")
    print("""
    1) Agregar estudiante
    2) Eliminar estudiante
    3) Salir
    """)

    opcion = input("Ingrese una opción: ")
    while not opcion.isdigit():
        print("Incorrecto. Debe ingresar un número.")
        opcion = input("Opción: ")

    match opcion:
        case "1":
            #Pedimos el nombre
            estudiante_nuevo = input("Ingrese el nombre del estudiante: ")
            #Verificamos que el nombre sea correcto
            while not estudiante_nuevo.isalpha():
                print("Error. Solo debe contener letras.")
                estudiante_nuevo = input("Ingrese el nombre del estudiante: ")
            estudiante_nuevo = estudiante_nuevo.capitalize()
            #Agregamos al estudiante a la lista
            estudiantes.append(estudiante_nuevo)
            print(f"Se agregó a {estudiante_nuevo} correctamente.")

        case "2":
            eliminar_estudiante = input("Ingrese el nombre del estudiante que desea eliminar: ")
            #Verificamos que el nombre sea correcto
            while not eliminar_estudiante.isalpha():
                print("Error. Solo debe contener letras.")
                eliminar_estudiante = input("Ingrese el nombre del estudiante: ")
            eliminar_estudiante = eliminar_estudiante.capitalize()
            if eliminar_estudiante in estudiantes:
                estudiantes.remove(eliminar_estudiante)
                print(f"Se eliminó a {eliminar_estudiante} correctamente.")
            else:
                print("El nombre ingresado no está en la lista.")

        case "3":
            print("Sesión cerrada. ")
            valor = False

        case _:
            print("Opción no válida. Debe ingresar 1, 2 o 3.")
            opcion = input("Ingrese una opción: ")

print("//////////////////////////////////////////////////////////////////////////////////////////////")

# EJERCICIO 6
#Lista con 7 números
#Rotar todas hacia la derecha (el ultimo pasa a ser el primero)

lista = [5, 6, 7, 8, 9, 10, 11]
print(f"Lista original: {lista}")

largo = len(lista)
ultimo = lista[largo-1] #Guardo el último numero para luego ponerlo en el indice 0

#Para cada índice, desde el ultimo al primero, lo paso un valor adelante
for i in range (largo-2,-1,-1):
    lista[i+1] = lista [i]

#Le asigno al indice 0, el valor que tenia guardado en la variable "ultimo"
lista[0] = ultimo

print("Rotar números hacia la derecha:")
print(lista)

print("//////////////////////////////////////////////////////////////////////////////////////////////")

#EJERCICIO 7:
#Crear matriz con temperaturas minimas y maximas de una semana
matriz_temperaturas = [
    [1, 14],
    [4, 20],
    [8, 19],
    [8, 18],
    [2, 13],
    [1, 3],
    [1, 7]
]

print(f"""Temperaturas mínimas y máximas de la semana:
Lunes: {matriz_temperaturas[0]}
Martes: {matriz_temperaturas[1]}
Miércoles: {matriz_temperaturas[2]}
Jueves: {matriz_temperaturas[3]}
Viernes: {matriz_temperaturas[4]}
Sábado: {matriz_temperaturas[5]}
Domingo: {matriz_temperaturas[6]}
""")

#Calcular el promedio de las mínimas y máximas
#Sumo valores
sumatoria_minimas = 0
sumatoria_maximas = 0

for i in range (len(matriz_temperaturas)):
    sumatoria_minimas += matriz_temperaturas[i][0]
    sumatoria_maximas += matriz_temperaturas[i][1]


#Promedio
promedio_minimas = sumatoria_minimas/len(matriz_temperaturas)
promedio_maximas = sumatoria_maximas/len(matriz_temperaturas)

print(f"""
Promedio mínimas: {promedio_minimas}
Promedio máximas: {promedio_maximas}
""")

#Día que registró mayor amplitud térmica
mayor_amplitud_termica = 0
for i in range (len(matriz_temperaturas)):

    amplitud_termica = matriz_temperaturas[i][1] - matriz_temperaturas[i][0]

    if amplitud_termica > mayor_amplitud_termica:
        mayor_amplitud_termica = amplitud_termica
        dia_mayor_amplitud_termica = i+1

print(f"El día que registró mayor amplitud térmica fue {dia_mayor_amplitud_termica}, con una diferencia de {mayor_amplitud_termica}.")

print("//////////////////////////////////////////////////////////////////////////////////////////////")

#EJERCICIO 8
#Matriz con las notas de 5  estudiantes, en 3 materias
matriz_estudiantes = [
    [7,9,10],
    [9,5,8],
    [6,10,7],
    [4,10,8],
    [9,9,10]
]

print(f"""Notas por estudiante en 3 materias:
Estudiante 1: {matriz_estudiantes[0]}
Estudiante 2: {matriz_estudiantes[1]}
Estudiante 3: {matriz_estudiantes[2]}
Estudiante 4: {matriz_estudiantes[3]}
Estudiante 5: {matriz_estudiantes[4]}
""")

for i in range (len(matriz_estudiantes)):
    promedio_estudiante = (matriz_estudiantes[i][0]+matriz_estudiantes[i][1]+matriz_estudiantes[i][2])/3
    print(f"El promedio del estudiante {i+1} es {promedio_estudiante}")
    

for i in range (len(matriz_estudiantes[0])):
    promedio_materia = (matriz_estudiantes[0][i]+matriz_estudiantes[1][i]+matriz_estudiantes[2][i]+matriz_estudiantes[3][i]+matriz_estudiantes[4][i])/5
    print(f"El promedio de la materia {i+1} es {promedio_materia} ")

print("//////////////////////////////////////////////////////////////////////////////////////////////")

# EJERCICIO 9
#Crear tablero
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
] 

print("TABLERO")
for i in range (len(tablero)):
    print(tablero[i][0], tablero[i][1], tablero[i][2])

# Turnos
jugador = "X"
cantidad_jugadas = 0
ganador = False

while cantidad_jugadas < 9 and (not ganador):
    print("-------------------------")
    print(f"Turno del jugador: {jugador}")
    print("-------------------------")

    fila =  input("Ingrese fila (1-3): ")
    while fila not in ("123"):
        print("Error. Debe ingresar solo números. 1, 2 o 3")
        fila = input("Ingrese número de fila: ")
    fila = int(fila)-1

    columna = input("Ingrese columna (1-3): ")
    while columna not in ("123"):
            print("Error. Debe ingresar solo números. 1, 2 o 3")
            columna = input("Ingrese número de columna: ")
    columna = int(columna)-1

    #Colocar X/O en el tablero
    while tablero[fila][columna] != "-":
        print("Casilla ocupada.")
        fila =  input("Ingrese fila (1-3): ")
        while fila not in ("123"):
            print("Error. Debe ingresar solo números. 1, 2 o 3")
            fila = input("Ingrese número de fila: ")
        fila = int(fila)-1

        columna = input("Ingrese columna (1-3): ")
        while columna not in ("123"):
                print("Error. Debe ingresar solo números. 1, 2 o 3")
                columna = input("Ingrese número de columna: ")
        columna = int(columna)-1
    tablero[fila][columna] = jugador

    cantidad_jugadas += 1

    #Mostrar tablero
    print("TABLERO")
    for i in range (len(tablero)):
        print(tablero[i][0], tablero[i][1], tablero[i][2])

    # Verificar filas:
    for i in range(3):
         if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
              ganador = True

    # Verificar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "-":
            ganador = True

    # Verificar diagonales:
    if tablero [0][0] == tablero[1][1] == tablero[2][2] != "-":
         ganador = True

    if tablero [0][2] == tablero[1][1] == tablero[2][0] != "-":
        ganador = True

    #Cambiar de jugador:
    if ganador == False:
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

if ganador == True:
     print(f"""
     -----------------------
     Ganó el jugador {jugador}!
     -----------------------
     """)
else:
     print("""
     --------
     Empate!
     --------
     """)

print("//////////////////////////////////////////////////////////////////////////////////////////////")

#EJERCICIO 10
matriz_ventas = [
    [30, 45, 15, 70, 50, 25, 40],  #Producto 1
    [40, 65, 71, 82, 94, 68, 37],  #Producto 2
    [59, 76, 31, 89, 10, 89, 85],  #Producto 3
    [55, 60, 22, 18, 30, 42, 35]   #Producto 4
]

print(f"""Cantidades vendidas por producto en 1 semana:
Producto 1: {matriz_ventas[0]}
Producto 2: {matriz_ventas[1]}
Producto 3: {matriz_ventas[2]}
Producto 4: {matriz_ventas[3]}
""")

# Total vendido por cada producto
for i in range (len(matriz_ventas)):
    total_producto = 0
    for j in range(len(matriz_ventas[i])):
        total_producto += matriz_ventas[i][j]
    print(f"El total vendido del producto {i+1} es {total_producto}")

# Día con mayores ventas totales
dia_mayor_venta = 0

for j in range(len(matriz_ventas[0])):
    total_dia = 0
    for i in range(len(matriz_ventas)):
        total_dia += matriz_ventas[i][j]
    if total_dia >dia_mayor_venta:
        dia_mayor_venta = total_dia
        dia = j+1
print(f"El día con mayores ventas totales fue el día {dia}, con {dia_mayor_venta} ventas. ")

# Producto más vendido de la semana
mayor_venta_producto = 0
for i in range (len(matriz_ventas)):
    total_producto = 0
    for j in range (len(matriz_ventas[i])):
        total_producto += matriz_ventas[i][j]
    if total_producto > mayor_venta_producto:
        mayor_venta_producto = total_producto
        producto_mas_vendido = i+1

print(f"El producto más vendido en la semana fue el {producto_mas_vendido}, con {mayor_venta_producto} ventas.")

print("//////////////////////////////////////////////////////////////////////////////////////////////")

# EJERCICIO 11
lista_estudiantes = ["Tomas", "Cristian", "Selene", "Joaquin", "Dylan", "Dafne", "Emiliano", "Abigail", "Morena", "Lucas"]
print(f"""Estudiantes:
{lista_estudiantes}
""")

# Ingresar estudiante a buscar
estudiante_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
while not estudiante_buscar.isalpha():
    print("Error. El nombre debe contener solo letras.")
    estudiante_buscar = input("Ingrese nuevamente el nombre del estudiante: ")
estudiante_buscar = estudiante_buscar.capitalize()

#Verificar que esté en la lista
if estudiante_buscar in (lista_estudiantes):
    print(f"{estudiante_buscar} si se encuentra en la lista de estudiantes.")

    # Mostrar la posición en que aparece
    for i in range(len(lista_estudiantes)):
        if lista_estudiantes[i] == estudiante_buscar:
            numero_posicion = i+1
            print(f"El estudiante se encuentra en la posición {numero_posicion}")
else:
    print(f"No se encontró a {estudiante_buscar} en la lista.")

print("//////////////////////////////////////////////////////////////////////////////////////////////")

# EJERCICIO 12
# Pedir al usuario 8 numeros enteros y almacenarlos en una lista
lista_numeros = []

for i in range(8):
    numero_lista = input(f"Ingrese el número {i+1} para añadir a la lista: ")
    while not numero_lista.isdigit():
        print("Debe ingresar un número entero.")
        numero_lista = input("Reintente. Ingrese el número: ")
    numero_lista = int(numero_lista)
    lista_numeros.append(numero_lista)
    print(f"Se añadió correctamente el número {numero_lista} a la lista.")

# Mostrar la lista original
print("Lista original:")
print(lista_numeros)

# Mostrar la lista menor a mayor
print("Lista ordenada de menor a mayor:")
lista_menor_mayor = sorted(lista_numeros)
print(lista_menor_mayor)

# Mostrar la lista mayor a menor
print("Lista ordenada de mayor a menor:")
lista_mayor_menor = sorted(lista_numeros, reverse=True)
print(lista_mayor_menor)

# EJERCICIO 13
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
print(puntajes)

# Mostrar el puntaje más alto y el más bajo
puntaje_alto = puntajes[0]
puntaje_bajo = puntajes[0]

for i in range(len(puntajes)):
    if puntajes[i] > puntaje_alto:
        puntaje_alto = puntajes[i]
    elif puntajes[i] < puntaje_bajo:
        puntaje_bajo = puntajes[i]

print(f"""
El puntaje más alto es {puntaje_alto}, y el más bajo es {puntaje_bajo}""")

# Lista ordenada de mayor a menor
ranking = sorted(puntajes, reverse=True)
print("Ranking (mayor a menor):")
print(ranking)

# En qué posicion del ranking se encuentra 990
for i in range(len(ranking)):
    if ranking[i] == 990:
        posicion_990 = i+1
        print(f"El puntaje 990 se encuentra en la posición {posicion_990} del ranking.")

print("//////////////////////////////////////////////////////////////////////////////////////////////")