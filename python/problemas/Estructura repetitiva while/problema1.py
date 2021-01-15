x=1
mayor=0
menor=0
while x<=10:
    nota=int(input("nota: "))
    if nota>=7:
        mayor=mayor+1
    else:
        menor=menor+1
    x=x+1
print("Notas mayores")
print(mayor)
print("Notas menores")
print(menor)