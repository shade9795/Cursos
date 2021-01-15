preguntas=int(input("Ingrese la cantidad de preguntas: "))
correctas=int(input("Ingrese la cantidad de respuestas correctas: "))

porcen=preguntas*correctas/100

if porcen>=90:
    print("Nivel Maximo")
else:
    if porcen>=75:
        print("Nivel Medio")
    else:
        if porcen>=50:
            print("Nivel Regular")
        else:
            print("Fuera de nivel")
