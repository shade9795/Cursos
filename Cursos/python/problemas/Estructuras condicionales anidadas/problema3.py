num=int(input("ingrese un numero de hasta tres cifras: "))

if num>1000:
    print("cifra exedida del limite")
else:
    if num>=100:
        print("tres cifras")
    else:
        if num>=10:
            print("dos cifras")
        else:
            print("una cifra")
        