num1=int(input("numero 1: "))
num2=int(input("numero 2: "))
num3=int(input("numero 3: "))

if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)