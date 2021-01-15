x=1
importe=0
conta1=0
conta2=0
empleados=int(input("Ingrese la cantidad de empleados: "))
while x<=empleados:
    sueldo=int(input("sueldo: "))

    if sueldo>=100 and sueldo<=300:
        conta1=conta1+1
    else:
        conta2=conta2+1

    importe=importe+sueldo
    x=x+1

print("sueldos entre 100 y 300")
print(conta1)
print("sueldos mayores a 300")
print(conta2)
print("importe total gastado en sueldos")
print(importe)