import numpy as np


productos = []

def validar_parte(num_parte):
    if len(num_parte) != 10:
        print("Error en el número de partes, el formato del número de partes es 999999-L99")
        return False
    elif num_parte[6] != "-":
        print("Error en el numero de partes, el formato del número de partes es 999999-L99")
        return False
    elif num_parte[7].isalpha() == False:
        print("Error en el numero de partes, el formato del número de partes es 999999-L99")
        return False
    elif num_parte[0:6].isnumeric() == False:
            #print(num_partes[0:6])
        print("Error en el numero de partes, el formato del número de partes es 999999-L99")
        return False
    elif num_parte[8:10].isnumeric() == False:
        print("Error en el numero de partes, el formato del número de partes es 999999-L99")
        return False
    return True

def grabar_partes():
    try:
        num_partes = input("Ingrese el numero de partes (999999-L99): ")
        if not validar_parte(num_partes):
            return

        nom_producto = input("Ingrese el nombre del producto: ")
        if len(nom_producto) < 6:
            print("Error en el nombre del producto, el nombre del producto debe ser mayor a 6 caracteres")
            return
        precio_producto = int(input("Ingrese el precio del producto: "))
        if precio_producto < 0:
            print("Error en el precio del producto, el precio del producto debe ser mayor a 0")
            return
        producto= [num_partes, nom_producto, precio_producto]
        productos.append(producto)
    except ValueError:
        print("Error en el ingreso de datos",ValueError)

def listar_partes():
    print("\tListado de partes")
    print("Número de Parte".ljust(20),"Nombre del Producto".ljust(20),"Precio del Producto".ljust(20))
    for producto in productos:
        print(producto[0].ljust(20),producto[1].ljust(20),str(producto[2]).ljust(20))

def buscar_partes():
    print("\tBuscar partes")
    arreglo = np.array(productos)
    num_parte= input("Ingrese el numero de parte: ")
    if not validar_parte(num_parte):
        print("Error en el numero de partes, el formato del número de partes es 999999-L99")
        return
    x = np.where(arreglo == num_parte)
    if x[0].size == 0:
        print("No se encontraron resultados")
        return
    else:
        print("Número de Parte".ljust(20),"Nombre del Producto".ljust(20),"Precio del Producto".ljust(20))
        print(str(*arreglo[x[0],0]).ljust(20),str(*arreglo[x[0],1]).ljust(20),str(*arreglo[x[0],2]).ljust(20))

def menu():
    try:
        print("\nMenu de opciones")
        print("1. Grabar partes")
        print("2. Buscar partes")
        print("3. Listar partes")
        print("4. Salir")
        opc = input("Ingrese la opcion: ")
        if opc == "1":
            grabar_partes()
        elif opc == "2":
            buscar_partes()
        elif opc == "3":
            listar_partes()
        elif opc == "4":
            exit()
        else:
            print("Opcion incorrecta")
    except ValueError :
        print("Error en la opcion", ValueError)

while True:
    menu()







