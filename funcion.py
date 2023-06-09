def sumar():
    num1=2
    num2=3
    res=num1*num2
    if res>10:
        return res
    else:
        return -1
    print("Hasta aqui llega la función")
    return res


res=sumar()
print("El resultado es",res)
