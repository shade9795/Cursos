sueldo=int(input("Sueldo: "))
antiguedad=int(input("antiguedad: "))

if sueldo<500 and antiguedad>=10:
    porcent=sueldo*20/100
    newsuel=sueldo+porcent
    print("aumento del 20%")
    print(newsuel)
else:
    if sueldo<500 and antiguedad<10:
        porcent=sueldo*5/100
        newsuel=sueldo+porcent
        print("aumento del 5%")
        print(newsuel)
    else:
        print("Sueldo a pagar sin aumento")
        print(sueldo)