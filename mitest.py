print("Bienvenido a mi test sobre patxi :D aaaaa")

puntuacion = 0

opcion = input("Pregunta 1: ¿Cual es la frase favorita de patxi\n"
               "A- aaa\n"
               "B- Estais muy equivocados\n"
               "C- Soy de carabanchel\n"
               "")
if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 15
else:
    print("Estas muy equivocado, las opciones son A, B y C")

opcion = input("Pregunta 2: ¿Cual es el hobbie favorito de patxi?\n"
               "A- Salir de clase y volver luego\n"
               "B- Salir de clase y no volver\n"
               "C- Access\n"
               "")
if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 15
else:
    print("Estas muy equivocado, las opciones son A, B y C")

opcion = input("Pregunta 3: ¿Cual es la asignatura que mejor enseña patxi\n"
               "A- Ofimatica\n"
               "B- Montaje\n"
               "C- Ninguna\n"
               "")
if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 15
else:
    print("Estas muy equivocado, las opciones son A, B y C")
    exit()

print("Tu puntuacion es:")
print(puntuacion)
print("Por lo cual...")

if puntuacion >= 35:
    print("¡Felicidades! Eres un patxi lover")
elif puntuacion >= 20:
    print("Eres amigo de patxi")
else:
    print("Patxi te cae muy mal por lo que veo")

print("Gracias por realizar este patxitest :D")
