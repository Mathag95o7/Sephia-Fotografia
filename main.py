import os
import sys
import calendar
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from clases.Citas import Citas
from clases.Fotografo import Fotografo
from clases.Cliente import Cliente

consola = Console()

def Limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    consola.input("\n[dim]Presiona ENTER para continuar...[/dim]")


def registro():
    print("\n------------Registro de Cliente------------")
    while True:
        comprobrar = True
        while comprobrar == True:
            CURP_reg = input("\nIngrese su CURP (18 caracteres): ")
            nombre_reg = input("\nIngrese su Nombre: ")
            telefono_reg = input("\nIngrese su Teléfono: ")
            email_reg = input("\nIngrese su Email: ")
            contra_reg = input("\nIngrese su contraseña (mín. 4 caracteres): ")
            compro = int(input("\nLos datos son correctos 1.Si 2.No: "))
            match compro:
                case 1:
                    comprobrar = False
                case 2:
                    comprobrar = True
                case _:
                    print("\nOpcion invalidad escoga un numero del 1-2 . ")
        try:
            cliente_nuevo = Cliente(CURP_reg, nombre_reg, telefono_reg, email_reg, contra_reg)
            cliente_nuevo.memoria()
            print("\nCliente registrado con éxito.")
            print(cliente_nuevo)
            break
        except ValueError as Err_curp:
            print(f"\nError en el registro: {Err_curp}")
            print("\nInténtelo de nuevo.")

def registro_fotografo():
    print("\n------------Registro de Fotógrafo------------")
    while True:
        comprobrar = True
        while comprobrar == True:    
            CURP_reg = input("\nIngrese su CURP (18 caracteres): ")
            nombre_reg = input("\nIngrese su Nombre: ")
            telefono_reg = input("\nIngrese su Teléfono: ")
            email_reg = input("\nIngrese su Email: ")
            contra_reg = input("\nIngrese su contraseña (mín. 4 caracteres): ")
            compro = int(input("\nLos datos son correctos 1.Si 2.No: "))
            match compro:
                case 1:
                    comprobrar = False
                case 2:
                    comprobrar = True
                case _:
                    print("\nOpcion invalidad escoga un numero del 1-2 . ")
        try:
            especial_reg = int(input("\nIngrese su especialidad (1. Videógrafo, 2. Fotógrafo, 3. Editor de fotos): "))
            match especial_reg:
                case 1:
                    especialidad = "Videógrafo"
                case 2:
                    especialidad = "Fotógrafo"
                case 3:
                    especialidad = "Editor de Fotos"
                case _:
                    print("\nOpción inválida. Se asignará 'Fotógrafo' por defecto.")
                    especialidad = "Fotógrafo"
        except ValueError:
            print("\nEntrada inválida. Debe ser un número.")
            continue

        try:
            fotografo_nuevo = Fotografo(CURP_reg, nombre_reg, telefono_reg, email_reg, contra_reg, especialidad)
            fotografo_nuevo.memoria_fotografo()
            print("\nFotógrafo registrado con éxito.")
            print(fotografo_nuevo)
            break
        except ValueError as Err_curp:
            print(f"\nError en el registro: {Err_curp}")
            print("\nInténtelo de nuevo.")

def inicio_sesion():
    print("\n------------Inicio de Sesión------------")
    try:
        Usuario = int(input("\n¿Quién desea iniciar sesión? (1. Cliente, 2. Fotógrafo): "))
    except ValueError:
        print("\nOpción inválida.")
        return

    match Usuario:
        case 1:
            if not Cliente.todos():
                print("\nNo hay clientes registrados, registre uno primero.")
                return
            curp_sesion = input("\nIngrese su CURP: ")
            contra_sesion = input("\nIngrese su contraseña: ")

            cliente_ini_sesion = Cliente.comprobacion(curp_sesion, contra_sesion)

            if cliente_ini_sesion:
                print(f"\nBienvenido de nuevo, {cliente_ini_sesion.nombre}.")
                control_usuario(cliente_ini_sesion)
            else:
                print("\nCURP o Contraseña incorrecta.")
        case 2:
            if not Fotografo.todos_fotografo():
                print("\nNo hay fotógrafos registrados, registre uno primero.")
                return
            curp_sesion = input("\nIngrese su CURP: ")
            contra_sesion = input("\nIngrese su contraseña: ")

            fotografo_ini_sesion = Fotografo.comprobacion_fotografo(curp_sesion, contra_sesion)

            if fotografo_ini_sesion:
                print(f"\nBienvenido de nuevo, {fotografo_ini_sesion.nombre}.")
                control_fotografo(fotografo_ini_sesion)
            else:
                print("\nCURP o Contraseña incorrecta.")
        case _:
            print("\nOpción no válida.")

def control_usuario(cliente):
    while True:
        print(f"\n------------Panel de Control - Cliente ({cliente.nombre})------------")
        print("\n1. Ver mis datos personales.")
        print("\n2. Menú citas.")
        print("\n3. Cerrar Sesión.")

        try:
            decision = int(input("\n¿Qué opción desea realizar? (1-3): ").strip())
        except ValueError:
            print("\nEntrada inválida.")
            continue

        match decision:
            case 1:
                print(f"\n{cliente}")
            case 2:
                menu_citas(cliente)
            case 3:
                print(f"\nSesión de {cliente.nombre} cerrada.")
                break
            case _:
                print("\nInválido: Escoja opción (1-3).")

def control_fotografo(fotografo):
    while True:
        print(f"\n------------Panel de Control - Fotógrafo ({fotografo.nombre})------------")
        print("\n1. Ver mis datos personales.")
        print("\n2. Ver mis citas asignadas.")
        print("\n3. Cerrar Sesión.")

        try:
            decision = int(input("\n¿Qué opción desea realizar? (1-3): ").strip())
        except ValueError:
            print("\nEntrada inválida.")
            continue

        match decision:
            case 1:
                print(f"\n{fotografo}")
            case 2:
                control_citas(fotografo)
            case 3:
                print(f"\nSesión de {fotografo.nombre} cerrada.")
                break
            case _:
                print("\nInválido: Escoja opción (1-3).")

def menu_citas(cliente):
    while True:
        print("\n------------Menú de Citas------------")
        print("\n1. Reservar cita.")
        print("\n2. Cancelar cita.")
        print("\n3. Ver mis citas.")
        print("\n4. Volver al panel principal.")

        try:
            eleccion = int(input("\nSelecciona una de las opciones (1-4): "))
        except ValueError:
            print("\nEntrada inválida.")
            continue

        match eleccion:
            case 1:
                reservar_citas(cliente)
            case 2:
                cancelar_citas(cliente)
            case 3:
                menu_vista_cita(cliente)
            case 4:
                break
            case _:
                print("\nOpción inválida.")

def reservar_citas(cliente):
    fotografos = Fotografo.todos_fotografo()
    if not fotografos:
        print("\nNo hay fotógrafos registrados en el sistema.")
        return

    print("\n------------Reservación de Citas------------")
    print("\nSelecciona a tu fotógrafo:")
    for i, f in enumerate(fotografos, 1):
        print(f"{i}. {f.nombre} ({f.especial})")

    try:
        seleccionar = int(input("\nNúmero de fotógrafo: "))
        if seleccionar < 1 or seleccionar > len(fotografos):
            print("\nSelección fuera de rango.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    fotografo_elegido = fotografos[seleccionar - 1]

    m = 10
    y = 2026
    while True:
        print(f"\n{calendar.month(y, m)}")
        dias_mes = calendar.monthrange(y, m)[1]
        try:
            decidir = int(input(f"\nSelecciona un día (1-{dias_mes}) o avanza de mes (0): "))
        except ValueError:
            print("\nEntrada inválida.")
            continue

        if decidir == 0:
            m += 1
            if m > 12:
                m = 1
                y += 1
        elif 1 <= decidir <= dias_mes:
            fecha_str = f"{decidir}/{m}/{y}"
            break
        else:
            print("\nDía no válido.")

    print("\nHorarios disponibles:")
    for hour in range(8, 20):
        print(f"{hour}:00 hrs")

    try:
        hora_seleccion = int(input("\nSeleccione la hora que desea la cita (8 - 19): "))
        if hora_seleccion < 8 or hora_seleccion > 19:
            print("\nHora fuera del rango laboral.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    nueva_cita = Citas(cliente.nombre, fotografo_elegido.nombre, fecha_str, str(hora_seleccion))
    print("\n¡Cita reservada con éxito!")
    print(nueva_cita)

def cancelar_citas(cliente):
    citas_todas = Citas.todas_citas()
    citas_cliente = [c for c in citas_todas if c.cliente_nombre == cliente.nombre]

    if not citas_cliente:
        print("\nNo tienes citas reservadas para cancelar.")
        return

    print("\n------------Cancelación de Citas------------")
    for i, cit in enumerate(citas_cliente, 1):
        print(f"{i}. {cit}")

    try:
        borrar = int(input(f"\n¿Cuál cita desea cancelar? (1-{len(citas_cliente)}): "))
        if 1 <= borrar <= len(citas_cliente):
            cita_a_borrar = citas_cliente[borrar - 1]
            Citas.lista_citas.remove(cita_a_borrar)
            print(f"\nLa cita ha sido cancelada: {cita_a_borrar}")
        else:
            print("\nSelección fuera de rango.")
    except ValueError:
        print("\nEntrada inválida.")

def menu_vista_cita(cliente):
    citas_todas = Citas.todas_citas()
    citas_cliente = [c for c in citas_todas if c.cliente_nombre == cliente.nombre]

    if not citas_cliente:
        print("\nNo tienes citas reservadas.")
        return

    print("\n------------Tus Citas Reservadas------------")
    for i, cit in enumerate(citas_cliente, 1):
        print(f"{i}. {cit}")

def control_citas(fotografo):
    citas_todas = Citas.todas_citas()
    citas_fotografo = [c for c in citas_todas if c.fotografo_elegido == fotografo.nombre]

    if not citas_fotografo:
        print("\nNo tienes citas asignadas.")
        return

    print("\n------------Citas Asignadas------------")
    for i, cit in enumerate(citas_fotografo, 1):
        print(f"{i}. {cit}")

def clientes_listar():
    clientes = Cliente.todos()
    if not clientes:
        print("\nNo hay ningún cliente registrado.")
        return

    print("\n------------Clientes Registrados------------")
    for i, c in enumerate(clientes, 1):
        print(f"{i}. {c.nombre} | CURP: {c.CURP} | Tel: {c.telefono} | Email: {c.email}")

def fotografo_listar():
    fotografos = Fotografo.todos_fotografo()
    if not fotografos:
        print("\nNo hay ningún fotógrafo registrado.")
        return

    print("\n------------Fotógrafos Registrados------------")
    for i, f in enumerate(fotografos, 1):
        print(f"{i}. {f.nombre} | Especialidad: {f.especial} | CURP: {f.CURP} | Tel: {f.telefono} | Email: {f.email}")

def ejecucion():
    while True:
        print("\n------------Sistema de Gestión de Citas------------")
        print("\n1. Registrar Cliente.")
        print("2. Registrar Fotógrafo.")
        print("3. Inicio de Sesión.")
        print("4. Ver lista de Clientes (Admin).")
        print("5. Ver lista de Fotógrafos (Admin).")
        print("6. Finalizar.")

        try:
            eleccion = int(input("\n¿Qué opción desea realizar? (1-6): ").strip())
        except ValueError:
            print("Entrada inválida, ingrese un número del 1 al 6.")
            continue

        match eleccion:
            case 1:
                registro()
            case 2:
                registro_fotografo()
            case 3:
                inicio_sesion()
            case 4:
                clientes_listar()
            case 5:
                fotografo_listar()
            case 6:
                print("\nBye\n")
                sys.exit(0)
            case _:
                print("\nOpción inválida. Escoja un número entre 1 y 6.")

if __name__ == "__main__":
    ejecucion()