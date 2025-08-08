import random
import time

print("Las reglas del juego son: \n"
"\tPiedra gana a Tijeras.\n" \
"\tTijeras gana a Papel.\n" \
"\tPapel gana a Piedra.\n")

while True:
    print("Elige una opción \n 1 - Piedra \n 2 - Papel \n 3 - Tijera")

    eleccion = int(input("Elige: "))

    while eleccion > 3 or eleccion < 1:
        eleccion = int(input("Elección no válida, elige de nuevo: "))

    if eleccion == 1:
        eleccion_nombre = "Piedra"
    elif eleccion == 2:
        eleccion_nombre = "Papel"
    elif eleccion == 3:
        eleccion_nombre = "Tijera"

    print("Has elegido: " + eleccion_nombre)
    print("Turno del ordenador.")

    eleccion_ord = random.randint(1,3)

    if eleccion_ord == 1:
        eleccion_ord_nombre = "Piedra"
    elif eleccion_ord == 2:
        eleccion_ord_nombre = "Papel"
    elif eleccion_ord == 3:
        eleccion_ord_nombre = "Tijera"

    print("Pensando...")
    time.sleep(3)
    
    print("El ordenador ha elegido: " + eleccion_ord_nombre)
    print(eleccion_nombre, " VS ", eleccion_ord_nombre)

    print("Calculando ganador...")
    time.sleep(3)

    gana_a = {
        1: [3],
        2: [1],
        3: [2]
    }
    
    if eleccion_nombre == eleccion_ord_nombre:
        resultado = "Empate"
    elif eleccion_ord in gana_a[eleccion]:
        resultado = eleccion_nombre
    else:
        resultado = eleccion_ord_nombre

    if resultado == "Empate":
        print("Hay un empate.")
    elif resultado == eleccion_nombre:
        print("¡Has ganado!")
    else:
        print("¡El ordenador ha ganado!")

    print("¿Quieres jugar de nuevo? (S/N)")
    jugar_nuevo = input().lower()
    if jugar_nuevo == "n":
        break

print("¡Gracias por jugar!")