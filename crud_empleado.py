import os
import json
os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)

def menu_general():
    os.system("cls")
    print("1. Crear empleado")
    print("2. Actualizar empleado")
    print("3. Eliminar empleado")
    print("4. Listar empleado")
    print("5. Salir")

def seleccionar_opcion(max_opcion):
    opcion = 0
    while True: 
        try:
            opcion = int(input("Seleccione una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opcion:
            input("Opción invalida intente nuevamente >> ")
        else:
            return opcion

def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)

        if opcion == 1:
            print("1. Crear empleado")
        elif opcion == 2:
            print("2. Actualizar empleado")
        elif opcion == 3:
            print("3. Eliminar empleado")
        elif opcion == 4:
            empleados = cargar_json('empleados.json')
            print(empleados)
        elif opcion == 5:
            return

        input()
        
iniciar_programa()