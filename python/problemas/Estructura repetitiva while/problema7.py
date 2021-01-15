x=1
pares=0
impares=0
while x<=6:
    valor=int(input("ingrese un valor: "))
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
    x=x+1

print("pares: ")
print(pares)
print("impares: ")
print(impares)