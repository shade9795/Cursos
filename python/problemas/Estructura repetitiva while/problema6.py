x=1
total1=0
total2=0

print("Primera lista")
while x<=5:
    valor=int(input("valor: "))
    total1=total1+valor
    x=x+1
    
x=1
print("Segunda lista")
while x<=5:
    valor1=int(input("valor: "))
    total2=total2+valor1
    x=x+1
    
if total1==total2:
    print("Listas iguales")
else:
    if  total1>total2:
        print("Lista 1 Mayor")
    else:
        print("lista 2 Mayor")
