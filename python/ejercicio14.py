nota1=int(input("ingrese nota 1: "))
nota2=int(input("ingrese nota 2: "))
nota3=int(input("ingrese nota 3: "))

prom=nota1+nota2+nota3/3

if prom>=7:
    print("Promocionado")
else:
    if prom>=4:
        print("regular")
    else:
        print("Reprobado")