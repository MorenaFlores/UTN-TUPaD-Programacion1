# EJERCICIO 1 ////////////////////////////////////////////////////////////////////////////////
print(">>>>>>>>>>>>>>>>> EJERCICIO 1 <<<<<<<<<<<<<<<<<<<")

#Pedir y validar nombre del cliente
nombre = input("Ingrese nombre del cliente: ")
    
while not nombre.isalpha():
    if nombre == "":
        print("Cadena vacía.")
        nombre = input("Ingrese nombre del cliente: ")
    else:
        print("Debe contener solo letras.")
        nombre = input("Reintente: ")

print(f"Bienvenido/a {nombre.capitalize()}")


#Pedir cantidad de productos a comprar
cantidad_productos = input("Ingrese cantidad de producto que desea comprar: ")

    
while not cantidad_productos.isdigit() or cantidad_productos == "0":
    print("Número no válido.")
    cantidad_productos = input("Ingrese un número entero positivo: ")

cantidad_productos = int(cantidad_productos)
print(cantidad_productos)


#Analisis por producto
total_con_descuento = 0
total_sin_descuento = 0

for i in range (1, cantidad_productos+1):
    precio = input(f"Ingrese precio del producto {i}: ")

    #Validar numero entero positivo
    while (not precio.isdigit()) or precio=="0":
        print("Precio no válido.")
        precio = input("Reintente (número entero positivo): ")
    precio=int(precio)

    descuento = input("Tiene descuento? (S/N): ")

    #Validar letras
    while descuento not in "sSnN":
        print("Respuesta no válida.")
        descuento = input("Ingrese S/N: ")

    if descuento=="s" or descuento=="S":
        total_sin_descuento += precio
        total_con_descuento += precio*0.9
    elif descuento=="n" or descuento=="N":
        total_sin_descuento += precio
        total_con_descuento += precio


#Imprimir resultados
print(f"""
Cliente: {nombre.title()}
Cantidad de productos: {cantidad_productos}

Total sin descuentos: ${total_sin_descuento:.2f}
Total con descuentos: ${total_con_descuento:.2f}

Ahorro: ${total_sin_descuento-total_con_descuento:.2f}

Promedio por producto: ${(total_con_descuento/cantidad_productos):.2f}""")

# EJERCICIO 2 /////////////////////////////////////////////////////////////////////////////////
print(">>>>>>>>>>>>>>>>> EJERCICIO 2 <<<<<<<<<<<<<<<<<<<")
usuario = "alumno"
clave = "python123"
intentos = 2

#Pedir datos
usuario_ingresado = input("Intento 1/3 - Usuario: ")
clave_ingresada = input("Clave: ")

#Verificar intentos y datos
while (usuario_ingresado != usuario or clave_ingresada != clave):
    if intentos>3:
        print("Cuenta bloqueada.")
        menu=False
        break
    elif usuario_ingresado!=usuario or clave_ingresada!=clave:
        print("Error. Datos incorrectos.")
        usuario_ingresado = input(f"Intento {intentos}/3 - Usuario: ")
        clave_ingresada = input("Clave: ")
    intentos += 1

if usuario_ingresado==usuario and clave_ingresada==clave:
    print("Acceso concedido.")
    print(f"Bienvenido/a {usuario}")
    menu = True

# Menú repetitivo
opcion = ""
while menu:
    print("""Menú
    1) Estado
    2) Cambiar clave
    3) Mensaje
    4) Salir""")

    opcion = input("Opcion: ")
    
    #Validar opcion
    while not opcion.isdigit():
        print("Error: Ingrese una opción válida (Solo números).")
        opcion = input("Opcion: ")

    opcion = int(opcion)

    #Opciones
    match opcion:
        case 1:
            print("Inscripto.")
            
        case 2:
            clave_nueva = input("Ingrese nueva clave (debe contener mínimo 6 caracteres): ")
            
            #Verifico clave nueva
            while len(clave_nueva)<6:
                print("La clave debe tener mínimo 6 caracteres.")
                clave_nueva = input("Ingrese una clave válida: ")
                
            #Confirmo clave y verifico que sean iguales
            confirmacion = input("Confirmar contraseña: ")
            if confirmacion==clave_nueva:
                print("Clave modificada correctamente.")
                clave = clave_nueva
            else:
                print("Rechazado")
            continue

        case 3:
            print("Siempre parece imposible hasta que se hace.")

        case 4:
            print("Hasta pronto! Gracias por acceder.")
            menu = False

        case _:
            print("Rango inválido.")
            opcion = input("Elija una opción (1-2-3-4): ")



# EJERCICIO 3 ///////////////////////////////////////////////////////////////////////////////
print(">>>>>>>>>>>>>>>>> EJERCICIO 3 <<<<<<<<<<<<<<<<<<<")
#Cupos fijos
lunes1 = "Libre"
lunes2= "Libre"
lunes3 = "Libre"
lunes4 = "Libre"
martes1 = "Libre"
martes2 = "Libre"
martes3 = "Libre"

turnos_disponibles_lunes = 4
turnos_disponibles_martes = 3

# Nombre del operador (solo letras):
nombre_operador = input("Ingrese nombre del operador: ")
while not nombre_operador.isalpha():
    print("Datos inválidos. Debe contener solo letras.")
    nombre_operador = input("Ingrese su nombre: ")
nombre_operador = nombre_operador.capitalize()

# Menú repetitivo
print(f"Bienvenido/a {nombre_operador}")
b = True
while b:
    print("""
    Menú:
    1) Reservar turno
    2) Cancelar turno
    3) Ver agenda del día
    4) Ver resumen general
    5) Cerrar sistema
        """)

    opcion = input("Opción que desea realizar: ") #Validar opción
    while not opcion.isdigit():
        print("Incorrecto. Ingrese solo el número.")
        opcion = input("Opción: ")

    match opcion:
        case "1":
            print("Días disponibles: 1)Lunes 2)Martes")
            dia_elegido_reservar = input("Elija el día del turno que quiera reservar: ")
            # Validar opcion día
            while dia_elegido_reservar!="1" and dia_elegido_reservar!="2":
                print("Dato inválido.")
                dia_elegido_reservar = input("Elija 1 o 2: ")
            dia_elegido_reservar = int(dia_elegido_reservar)

            # Nombre del paciente
            nombre_paciente = input("Ingrese nombre del paciente: ")
            # Validar solo letras 
            while not nombre_paciente.isalpha():
                print("Datos inválidos. El nombre debe contener solo letras.")
                nombre_paciente = input("Reintente. Ingrese nombre del paciente: ")
            nombre_paciente = nombre_paciente.capitalize()



            # Verificar que no esté repetido en ese día y reservar el primer turno disponible
            if dia_elegido_reservar == 1 and nombre_paciente not in (lunes1, lunes2, lunes3, lunes4):
                if lunes1 == "" or lunes1 == "Libre":
                    lunes1 = nombre_paciente
                    turnos_disponibles_lunes -= 1
                    print(f"Turno reservado con éxito.\n {nombre_paciente} - Día: Lunes - Turno 1")
                elif lunes2 == "" or lunes2 == "Libre":
                    lunes2 = nombre_paciente
                    turnos_disponibles_lunes -= 1
                    print(f"Turno reservado con éxito.\n {nombre_paciente} - Día: Lunes - Turno 2")
                elif lunes3 == "" or lunes3 == "Libre":
                    lunes3 = nombre_paciente
                    turnos_disponibles_lunes -= 1
                    print(f"Turno reservado con éxito.\n {nombre_paciente} - Día: Lunes - Turno 3")
                elif lunes4 == "" or lunes4 == "Libre":
                    lunes4 = nombre_paciente
                    turnos_disponibles_lunes -= 1
                    print(f"Turno reservado con éxito.\n {nombre_paciente} - Día: Lunes - Turno 4")
                else:
                    if "Libre" in (martes1, martes2, martes3):
                        print("Día ocupado. Hay turnos disponibles el día -Martes-")
                    else:
                        print("Disculpe. Ambos días están ocupados, intente en otro momento.")
                continue
            elif nombre_paciente in (lunes1, lunes2, lunes3, lunes4):
                print("Paciente ya registrado este día.")

            if dia_elegido_reservar == 2 and nombre_paciente not in (martes1, martes2, martes3):
                if martes1 == "" or martes1 == "Libre":
                    martes1 = nombre_paciente
                    turnos_disponibles_martes -= 1
                    print(f"Turno reservado con éxito.\n {nombre_paciente} - Día: Martes - Turno 1")
                elif martes2 == "" or martes2 == "Libre":
                    martes2 = nombre_paciente
                    turnos_disponibles_martes -= 1
                    print(f"Turno reservado con éxito.\n {nombre_paciente} - Día: Martes - Turno 2")
                elif martes3 == "" or martes3 == "Libre":
                    martes3 = nombre_paciente
                    turnos_disponibles_martes -= 1
                    print(f"Turno reservado con éxito.\n {nombre_paciente} - Día: Martes - Turno 3")
                else:
                    if "Libre" in (lunes1, lunes2, lunes3, lunes4):
                        print("Día ocupado. Hay turnos disponibles el día -Lunes-")
                    else:
                        print("Disculpe. Ambos días están ocupados, intente en otro momento.")
                continue
            elif nombre_paciente in (martes1, martes2, martes3):
                print("Paciente ya registrado este día.")
        
        case "2":
            print("Días de turnos: 1)Lunes 2)Martes")
            dia_elegido_cancelar = input("Elija el día del turno que desea cancelar: ")
            # Validar opcion día
            while dia_elegido_cancelar!="1" and dia_elegido_cancelar!="2":
                print("Día inválido.")
                dia_elegido_cancelar = input("Elija 1 o 2: ")
            dia_elegido_cancelar = int(dia_elegido_cancelar)

            # Nombre del paciente
            nombre_paciente_cancelar = input("Ingrese nombre del paciente que desea cancelar: ")
            # Validar solo letras 
            while not nombre_paciente_cancelar.isalpha():
                print("Datos inválidos. El nombre debe contener solo letras.")
                nombre_paciente_cancelar = input("Reintente. Ingrese nombre del paciente: ")
            nombre_paciente_cancelar = nombre_paciente_cancelar.capitalize()

            # Si existe, cancelar y dejar el espacio vacío ("")
            if dia_elegido_cancelar == 1:
                if nombre_paciente_cancelar in lunes1:
                    lunes1 = "Libre"
                    turnos_disponibles_lunes += 1
                    print(f"Se canceló correctamente el turno de {nombre_paciente_cancelar}.")
                elif nombre_paciente_cancelar in lunes2:
                    lunes2 = "Libre"
                    turnos_disponibles_lunes += 1
                    print(f"Se canceló correctamente el turno de {nombre_paciente_cancelar}.")
                elif nombre_paciente_cancelar in lunes3:
                    lunes3 = "Libre"
                    turnos_disponibles_lunes += 1
                    print(f"Se canceló correctamente el turno de {nombre_paciente_cancelar}.")
                elif nombre_paciente_cancelar in lunes4:
                    lunes4 = "Libre"
                    print(f"Se canceló correctamente el turno de {nombre_paciente_cancelar}.")
                else:
                    print("Paciente no encontrado este día. Intentente nuevamente.")

            if dia_elegido_cancelar == 2:
                if nombre_paciente_cancelar in martes1:
                    martes1 = ""
                    turnos_disponibles_martes += 1
                    print(f"Se canceló correctamente el turno de {nombre_paciente_cancelar}.")
                elif nombre_paciente_cancelar in martes2:
                    martes2 = ""
                    turnos_disponibles_martes += 1
                    print(f"Se canceló correctamente el turno de {nombre_paciente_cancelar}.")
                elif nombre_paciente_cancelar in martes3:
                    martes3 = ""
                    turnos_disponibles_martes += 1
                    print(f"Se canceló correctamente el turno de {nombre_paciente_cancelar}.")
                else:
                    print("Paciente no encontrado este día. Intentente nuevamente.")
        
        case "3":
            # Mostrar los turnos del día en orden
            # Indicar "libre" si está vacío
            print(f"""
            ___________________________________
            Lunes - Turno 1 : {lunes1}
            Lunes - Turno 2 : {lunes2}
            Lunes - Turno 3 : {lunes3}
            Lunes - Turno 4 : {lunes4}
            -----------------------------------
            Martes - Turno 1 : {martes1}
            Martes - Turno 2 : {martes2}
            Martes - Turno 3 : {martes3}
            __________________________________""")

        case "4":
            # Turnos ocupados y disponibles por día
            # Días con más turnos (o empate) 
            turnos_ocupados_lunes = 4-turnos_disponibles_lunes
            turnos_ocupados_martes = 3-turnos_disponibles_martes
            print(f"""
            >>> Día LUNES <<<
            -Turnos disponibles: {turnos_disponibles_lunes}
            -Turnos ocupados: {turnos_ocupados_lunes}
            >>> Día MARTES <<<
            -Turnos disponibles: {turnos_disponibles_martes}
            -Turnos ocupados: {turnos_ocupados_martes}
            """)
            if turnos_ocupados_lunes>turnos_ocupados_martes:
                print("LUNES es el día con más turnos.")
            else:
                print("MARTES es el día con más turnos.")
            pass        

        case "5":
            print("Hasta luego. Cesión cerrada.")
            b=False


# EJERCICIO 4 //////////////////////////////////////////////////////////////////////////////
print(">>>>>>>>>>>>>>>>> EJERCICIO 4 <<<<<<<<<<<<<<<<<<<")
# ESCAPE ROOM: LA BÓVEDA
# Misión: Abrir una bóveda con 3 cerraduras / Energía y tiempo limitados

# Variable iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

# Pedir nombre y validar
nombre_agente = input("Ingrese su nombre: ")
while not nombre_agente.isalpha():
    print("Datos inválidos. El nombre debe contener solo letras")
    nombre_agente = input("Reintente. Ingrese su nombre: ")
nombre_agente = nombre_agente.capitalize()
print(f"--- BIENVENIDO/A {nombre_agente} --- Que comience el juego!")

# Menú de acciones
while energia>0 and tiempo>0 and cerraduras_abiertas<3 and alarma==False:
    print(f"""
    --------------------------
    Energía = {energia}
    Tiempo = {tiempo}
    Cerraduras abiertas = {cerraduras_abiertas}
    --------------------------
    >>> Menú <<<
    1) Forzar cerradura
    2) Hackear panel
    3) Descansar
     """)

    #Elegir acción y verificar dígito
    accion_elegida = input("Elija la acción que desea realizar: ")
    while not accion_elegida.isdigit():
        print("Datos inválidos.")
        accion_elegida = input("Ingrese el número de la acción: ")
    accion_elegida = int(accion_elegida)

    match accion_elegida:
        # Forzar cerradura (-20 energía / -2 tiempo)
        case 1:
            energia -= 20
            tiempo -= 2
            forzar_seguidas += 1
            if forzar_seguidas == 3:
                print(">>> Alarma activada. La cerradura se trabó.")
                forzar_seguidas -= 1
                if tiempo<=3:
                    print("-DERROTA(Bloqueo)- La alarma está activada y no tienes tiempo.")
                    break
            elif energia<40:
                print("Riesgo de alarma.")
                #Elegir numero de suerte y validar
                numero_suerte = input("Elija un número del 1 al 3: ")
                while (not numero_suerte.isdigit()) or numero_suerte not in "123":
                    print("Datos inválidos. Debe ingresar 1, 2 o 3")
                    numero_suerte = input("Elija: ")
                # Si elige 3 -> alarma=True
                if numero_suerte == "3":
                    alarma = True
                    print(">>> Alarma activada.")
                else:
                    alarma = False
                    cerraduras_abiertas += 1
                    print(">>> Tuviste suerte. Abriste una cerradura!")
            else:
                cerraduras_abiertas += 1
                print(">>> Tuviste suerte. Abriste una cerradura!")
                continue

        #Hackear panel (-10 energía / -3 tiempo)
        case 2:
            energia -= 10
            tiempo -= 3
            forzar_seguidas = 0
            for i in range (1,5):
                letra = input(f"{i} - Escibra una letra: ")
                while not letra.isalpha() or len(letra)>1:
                    print("Datos inválidos. Debe ingresar solo 1 letra.")
                    letra = input("Ingrese la letra: ")
                letra = letra.upper()
                codigo_parcial += letra
                print(f"El código parcial es: {codigo_parcial}")

            if len(codigo_parcial)>=8:
                cerraduras_abiertas += 1
                print(">>> Que suerte! Abriste una cerradura.")
                continue
            else:
                print(">>> La cerradura todavía no se abre.")
                continue

        # Descansar
        case 3:
            forzar_seguidas = 0
            tiempo -= 1
            energia += 15
            if energia>100:
                energia = 100
            if alarma == True:
                energia -= 10
            print(">>> Recuperaste energia.")
            continue
        # Rango inválido
        case _:
            print("Rango inválido. Debe ingresar el número de la acción (1, 2 o 3)")
            accion_elegida = input("Seleccione: ")
            continue
    
    if alarma == True and tiempo<=3:
        print("-DERROTA(Bloqueo)- La alarma está activada y no tienes tiempo.")
        break

print(f"""
--------------------------
Energía = {energia}
Tiempo = {tiempo}
Cerraduras abiertas = {cerraduras_abiertas}
--------------------------
""")
if cerraduras_abiertas == 3:
    print(">>>> ¡VICTORIA! <<<<")
if energia<=0:
    print(">>>> DERROTA <<<< Te quedaste sin energía.")
if tiempo<=0:
    print(">>>> DERROTA <<<< Te quedaste sin tiempo.")

# EJERCICIO 5 ///////////////////////////////////////////////////////////////////////////////////
# ESCAPE ROOM: La arena del gladiador
print(">>>>>>>>>>>>>>>>> EJERCICIO 5 <<<<<<<<<<<<<<<<<<<")
# Configuración del personaje. 
# Nombre del gladiador y validación
nombre_gladiador :str = input("Ingrese su nombre: ")
while not nombre_gladiador.isalpha():
    print("Error. Solo se permiten letras.")
    nombre_gladiador :str = input("Ingrese su nombre: ")
nombre_gladiador :str = nombre_gladiador.upper()

print(f"--- BIENVENIDO/A A LA ARENA {nombre_gladiador} ---")

# Inicialización de estadísticas
# Variables iniciales
vida_gladiador :int = 100
vida_enemigo :int = 100
pociones_vida :int = 3
danio_ataque_pesado :int = 15
danio_enemigo :int = 12
turno_gladiador :bool = True

while vida_gladiador>0 and vida_enemigo>0 and turno_gladiador:
        print(f"""
        ------------------------------
        Vida actual gladiador: {vida_gladiador}
        Vida actual enemigo: {vida_enemigo}
        ------------------------------
        >>>>> Menú <<<<<
        1. Ataque pesado
        2. Ráfaga Veloz
        3. Curar
        """)

        opcion :str = input("Acción que desea realizar: ")
        while not opcion.isdigit():
            print("Error. Debe ingresar solo el número de la acción (1, 2 o 3)")
            opcion :str = input ("Acción que desea realizar: ")

        match opcion:
            case "1": # Ataque pesado
                if vida_enemigo<20:
                    danio_ataque_pesado = danio_ataque_pesado * 1.5
                    vida_enemigo -= danio_ataque_pesado
                else:
                    vida_enemigo -= danio_ataque_pesado
                print(f"\n>¡Atacaste al enemigo por {danio_ataque_pesado} puntos de daño!")
                turno_gladiador = False

            case "2": # Ráfaga veloz
                for i in range (1,4):
                    vida_enemigo -= 5
                    print(">Golpe conectado por 5 de daño")
                turno_gladiador = False

            case "3": # Curar
                if pociones_vida>0:
                    vida_gladiador += 30
                    pociones_vida -= 1
                    if vida_gladiador >= 100:
                        vida_gladiador = 100
                    print(f"""
                    Recuperaste vida!
                    ------------------------------
                    Vida actual gladiador: {vida_gladiador}
                    ------------------------------
                    Ten cuidado, te quedan {pociones_vida} pociones.""")
                else:
                    print("\n¡No te quedan pociones! (pierdes el turno)")
                    
                
                turno_gladiador = False

            case _:
                print("Rango inválido. Debe elegir 1, 2 o 3 ")
                opcion = input("Acción que desea realizar: ")
                continue

        if vida_gladiador<=0 or vida_enemigo<0:
            break

        # Turno enemigo:
        vida_gladiador -= danio_enemigo
        print(f"\n>>¡El enemigo atacó por {danio_enemigo} puntos de daño!")
        turno_gladiador = True

if vida_gladiador<0:
    vida_gladiador = 0
if vida_enemigo<0:
    vida_enemigo = 0

# Fin del juego: 
if vida_gladiador >0:
    print(f"""
    ¡VICTORIA! {nombre_gladiador} ha ganado la batalla.
    ------------------------------
    Vida final gladiador: {vida_gladiador}
    Vida final enemigo: {vida_enemigo}
    ------------------------------""")
elif vida_gladiador == 0:
    print(f"""
    DERROTA. Has caído en combate
    ------------------------------
    Vida final gladiador: {vida_gladiador}
    Vida final enemigo: {vida_enemigo}
    ------------------------------""")