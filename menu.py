def menu():
    sw=0
    while sw==0:
        try:
            print("\tMenú de funciones")
            print("1.- Calcular IVA")
            print("2.- Descuento de producto")
            print("3.- Calcular IMC")
            print("4.- Salir")
            op=int(input("Ingrese una opción: "))
            if op==1:
                calcular_iva()
                #llamar a Calcular Iva
            elif op==2:
                descuento()
                #llamar a Descuento
            elif op==3:
                calcular_imc()
                #llamar a IMC
            elif op==4:
                sw=1
                print("\nSaliendo del Sistema")
            else:
                print("Debe ingresar un valor entre 1 y 4\n")
        except:
            print("Ingrese un número entre 1 y 4 como opción")

def calcular_iva():
    sw=0
    while sw==0:
        try:
            print("\nBienvenido al cálculo de IVA")
            neto=int(input("Ingrese el valor neto del producto: "))
            iva=neto*0.19
            print(f"El valor del iva del producto es {iva}\n")
            sw=1
        except:
            print("Debe ingresar un número\n") 

def descuento():
    sw=0
    while sw==0:
        try:
            print("\nBienvenido al cálculo de Descuento")
            producto=int(input("Ingrese el valor del producto: "))
            porcentaje=int(input("Ingrese el porcentaje de descuento: "))
            descuento=producto-(producto*porcentaje/100)
            print(f"El valor del producto con descuento es {descuento}\n")
            sw=1
        except:
            print("Debe ingresar un número en ambas opciones\n")

def calcular_imc():
    sw=0
    while sw==0:
        try:
            print("\nBienvenido al cálculo de IMC")
            altura=float(input("Ingrese su altura en metros: "))
            peso=int(input("Ingrese su peso en Kgs: "))
            imc=peso/(altura*altura)
            print(f"Su IMC es {imc}\n")
            if imc<18.5:
                print("Usted tiene bajo peso")
            elif imc>=18.5 and imc<=24.9:
                print("Usted tiene un peso normal")
            elif imc>=25 and imc<=29.9:
                print("Usted tiene sobrepeso")
            elif imc>=30 and imc<=34.9:
                print("Usted tiene obesidad tipo 1")
            elif imc>=35 and imc<=39.9:
                print("Usted tiene obesidad tipo 2")
            elif imc>=40:
                print("Usted tiene obesidad tipo 3")
            sw=1
        except:
            print("Debe ingresar un número para la altura y peso\n")

menu()