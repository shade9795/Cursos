x=int(input("Cordenada X: "))
y=int(input("Cordenada Y: "))

if x==0 or y==0:
    print("Las coordenadas deben ser diferentes a 0")
else:
    if x>0 and y>0:
        print("1º Cuadrante")
    else:
        if x<0 and y>0:
            print("2º Cuadrante")