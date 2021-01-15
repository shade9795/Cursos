num=int(input("Ingrese un numero del 1 al 99: "))
if num<10:
    print("su numero tiene una cifras")
else:
    if num<100:
        print("su numero tiene dos cifras")
    else:
        print("el numero ingresado supera la medida establecida")
