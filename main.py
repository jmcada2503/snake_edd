import pygame
import sys
import random
import time
from collections import deque
import threading

pygame.init()
# ancho y largo
Ancho, Largo = [300, 300]

# Tamaño de la pantalla
size = (Ancho, Largo)

# Colores
Blanco = (255, 255, 255)
Gris = (128, 128, 128)
Verde = (0, 200, 0)
Rojo = (255, 0, 0)
Negro = (0, 0, 0)

# fps
Fps = pygame.time.Clock()
# ventana
screen = pygame.display.set_mode(size)
# cordenadas
cord_x = ((Ancho//15)//2)*15
cord_y = ((Largo//15)//2)*15
# velocidad
velocidad = 15

posicion = [cord_x, cord_y]
cuerpo = deque([[cord_x, cord_y], [cord_x, cord_y+15], [cord_x, cord_y+30]])
direccion = 'up'
# run = True
food = [225, 60]
puntuacion = 0
crono = time.time()

# Funcion para la generacion de los puntos
def rand_food(cuerp, food):
    r1 = random.randint(0, (Ancho//15)-1)*15
    r2 = random.randint(0, (Largo//15)-1)*15
    a = True
    for body in cuerp:
        if body[0] != r1 and body[1] != r2:
            a = True
        else:
            a = False
            break
    if a == True:
        food[0] = r1
        food[1] = r2
    else:
        rand_food(cuerp, food)

# Funcion para validar si choca con su propio cuerpo
def colisionPropioCuerpo(posicion, cuerpo):
    return True if posicion in [cuerpo[i] for i in range(1, len(cuerpo))] else False

# Funcion para validar que no se devuelva sobre su propio cuerpo
def getNuevaDireccion(direccion, nuevaDireccion):
    validDirections = {
        'up': ['right', 'left'],
        'down': ['right', 'left'],
        'right': ['up', 'down'],
        'left': ['up', 'down']
    }
    if nuevaDireccion in validDirections[direccion]:
        return (nuevaDireccion, True)
    return (direccion, False)


flagDireccion = False
comio = False
comidaPosicionVieja = food.copy()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Jugaste", str(round(time.time()-crono)), "segundos")
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not flagDireccion:
                direccion, flagDireccion = getNuevaDireccion(direccion, 'up')
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not flagDireccion:
                direccion, flagDireccion = getNuevaDireccion(direccion, 'down')
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not flagDireccion:
                direccion, flagDireccion = getNuevaDireccion(direccion, 'right')
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not flagDireccion:
                direccion, flagDireccion = getNuevaDireccion(direccion, 'left')

    if direccion == 'up':
        posicion[1] -= velocidad
    if direccion == 'down':
        posicion[1] += velocidad
    if direccion == 'right':
        posicion[0] += velocidad
    if direccion == 'left':
        posicion[0] -= velocidad
    cuerpo.appendleft(posicion.copy())
    
    #aparicion nueva comida
    if (food[0] == posicion[0] and food[1] == posicion[1]):
        comidaPosicionVieja = food.copy()
        comio = True
        threading.Timer(
            random.randint(0, 9),
            rand_food,
            args=(cuerpo, food,)
        ).start()

        puntuacion += 1
        print(puntuacion)
    else:
        cuerpo.pop()

    #fin del juego si colisiona contra los bordes de la pantalla o con su propio cuerpo
    if ((posicion[0] < 0) or (posicion[0] >= Ancho) or (posicion[1] < 0) or (posicion[1] >= Largo) or (colisionPropioCuerpo(posicion, cuerpo))):
        print("Jugaste", str(round(time.time()-crono)), "segundos")
        break

    # dibuja la pantalla, la serpiente y la comida
    screen.fill(Negro)
    for body in cuerpo:
        pygame.draw.rect(screen, Gris, (body[0], body[1], 15, 15))
    if comidaPosicionVieja != food or not comio:
        pygame.draw.rect(screen, Rojo, (food[0], food[1], 15, 15))
        comio = False
    # Actualiza la pantalla
    pygame.display.flip()
    Fps.tick(8)
    flagDireccion = False
