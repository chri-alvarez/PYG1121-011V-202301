def sumar(a,b=7):
    suma=a+b
    return(suma)

num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese un número: "))

suma=13
print("El resultado de la suma es",sumar(num1,num2))
print("El valor de la suma es",suma)

sumar(num1,num2)
sumar(12,13)
sumar(4)