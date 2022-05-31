calificacion = int(input("Ingresa tu calificacion de  la AZ-900: "))
if calificacion <= 700:
    print("Reprobaste por no estudiar")
elif 800 <= calificacion <= 900:
    print("Aprobaste, pero te falta practicar")
elif 900 <= calificacion <= 1000:
    print("Excelente, estas en la mejor calificacion")
else:
    print("No esta en el rango")