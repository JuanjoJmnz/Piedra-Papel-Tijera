import random
import time

vidaJugador = 100
vidaPC = 100

print("¡Que comience el combate!")

print(f"\nEl jugador tiene {vidaJugador} puntos de vida y el PC tiene {vidaPC} puntos de vida.")

while vidaJugador > 0 and vidaPC > 0:
    print("\nTurno del jugador:")
    print("1. Ataque ligero (5-15 puntos de daño) | 2. Ataque fuerte (8-25 puntos de daño) | 3. Curarse (10-20 puntos de vida)")
    accion = input("Elige tu acción (1, 2 o 3): ")

    if accion == "1":
        danio = random.randint(5, 15)
        vidaPC -= danio
        if danio == 15:
            print("¡Golpe crítico!")
        print(f"¡Has infligido {danio} puntos de daño al PC!")

    elif accion == "2":
        danio = random.randint(8, 25)
        vidaPC -= danio
        if danio == 25:
            print("¡Golpe crítico!")
        print(f"¡Has infligido {danio} puntos de daño al PC!")

    elif accion == "3" and vidaJugador == 100:
        print("No puedes curarte, ya tienes la vida completa.")

    elif accion == "3":
        curacion = random.randint(10, 20)
        if vidaJugador + curacion > 100:
            vidaJugador = 100
        else:
            vidaJugador += curacion
        if curacion == 20:
            print("¡Curación crítica!")
        print(f"¡Te has curado {curacion} puntos de vida!")
        print(f"Vida del jugador: {vidaJugador}")
    else:
        print("Acción no válida. Inténtalo de nuevo.")
        continue

    if vidaPC < 0:
        vidaPC = 0
        print("¡Has ganado!")
        print(f"Vida del PC: {vidaPC}")
        break

    print(f"Vida del PC: {vidaPC}")

    time.sleep(3)


    print("\nTurno del PC:")
    accionPC = random.choice(["1", "2", "3"])
    print(f"El PC ha elegido la acción: {accionPC}")

    if accionPC == "1":
        danioPC = random.randint(5, 15)
        vidaJugador -= danioPC
        if danioPC == 15:
            print("¡Golpe crítico del PC!")
        print(f"¡Se han infligido {danioPC} puntos de daño al Jugador!")

    elif accionPC == "2":
        danioPC = random.randint(8, 25)
        vidaJugador -= danioPC
        if danioPC == 25:
            print("¡Golpe crítico del PC!")
        print(f"¡Se han infligido {danioPC} puntos de daño al Jugador!")

    elif accionPC == "3" and vidaPC == 100:
        print("No puede curarse, ya tiene la vida completa.")
    elif accionPC == "3":
        curacionPC = random.randint(10, 20)
        if vidaPC + curacionPC > 100:
            vidaPC = 100
        else:
            vidaPC += curacionPC
        if curacionPC == 20:
            print("¡Curación crítica del PC!")
        print(f"¡El PC se ha curado {curacionPC} puntos de vida!")
        print(f"Vida del PC: {vidaPC}")

    else:
        print("Acción no válida. Inténtalo de nuevo.")
        continue

    if vidaJugador < 0:
        vidaJugador = 0
        print("¡El PC ha ganado!")
        print(f"Vida del jugador: {vidaJugador}")
        break

    print(f"Vida del jugador: {vidaJugador}")
    
    time.sleep(3)

    print("\n\n-- Fin del turno --\n")