
c=0
while True:
    print("ingrese el numero de opeacion a realizar:")
    print("1.suma")
    print("2.resta")
    print("3.multiplicaion")
    print("4.division")
    print("5.salir")
    c=int(input("ingrese el numero de operaccion seleccionada: "))
    if c == 1:
        print("ingrese los datos solicitados:")
        a=int(input("Ingrese un primer numero:"))
        b=int(input("ingrese un segundo numero:"))
        resultado=a+b
        print("el resultado es",":",resultado)
    elif c == 2:
        print("ingrese los datos solicitados:")
        a=int(input("Ingrese un primer numero:"))
        b=int(input("ingrese un segundo numero:"))
        resultado=a-b
        print("el resultado es",":",resultado)
    elif c == 3:
        print("ingrese los datos solicitados:")
        a=int(input("Ingrese un primer numero:"))
        b=int(input("ingrese un segundo numero:"))
        resultado= a*b
        print("el resultado es",":",resultado)
    elif c==4:
        print("ingrese los datos solicitados:")
        a=int(input("Ingrese un primer numero:"))
        b=int(input("ingrese un segundo numero:"))
        resultado=a/b
        print("el resultado es",":",resultado)
    elif c== 5:
        break
    else:
        print("Seleccione lguna opcion")
