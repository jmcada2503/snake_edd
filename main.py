import pygame , sys
import random
import time
from collections import deque

pygame.init()
#ancho y largo
Ancho,Largo= [300,300]


#Tamaño de la pantalla
size=(Ancho, Largo)

#Colores
Blanco= (255,255,255)
Gris=(128,128,128)
Verde=(0,200,0)
Rojo=(255,0,0)

#fps
Fps=pygame.time.Clock()

#ventana
screen= pygame.display.set_mode(size)

fuente= pygame.font.SysFont("arial",25)

#cordenadas
cord_x=((Ancho//15)//2)*15
cord_y=((Largo//15)//2)*15
#velocidad
velocidad=15

direccion=''
#Funcion para la generacion de los puntos
def rand_food(cuerp):
        r1=random.randint(0,(Ancho//15)-1)*15
        r2=random.randint(0,(Largo//15)-1)*15
        a=True
        for body in cuerp:
             if body[0]!=r1 and body[1]!=r2:
                  a=True
             else:
                  a=False
                  break
        if a==True:
             posicion=[r1,r2]
        else:
             posicion=rand_food(cuerp)
        return posicion

# def cronometro(run):
#      inicio=time.time()
#      if run==False:
#           fin=time.time()
#           tiempo=round(fin-inicio)
#           return print("El tiempo que jugaste fue de", str(tiempo)+"s")

posicion = [cord_x, cord_y]
cuerpo = deque([[cord_x,cord_y],[cord_x,cord_y+15],[cord_x,cord_y+30]])
direccion = 'up'
# run = True
food = [225, 60]
puntuacion = 0
crono=time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Jugaste",str(round(time.time()-crono)),"segundos")
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                direccion = 'up'
            if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                direccion = 'down'
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                direccion = 'right'
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                direccion = 'left'
    
    if direccion == 'up':
        posicion[1] -= velocidad
    if direccion == 'down':
        posicion[1] += velocidad
    if direccion == 'right':
        posicion[0] += velocidad
    if direccion == 'left':
        posicion[0] -= velocidad

    cuerpo.appendleft(posicion.copy())

#        if ((food[0]-10) <= posicion[0] <= (food[0]+10)) and ((food[1]-10) <= posicion[1] <= (food[1]+10)):
    if (food[0] == posicion[0] and food[1] == posicion[1]):
        food = rand_food(cuerpo)
        puntuacion += 1
        print(puntuacion)
    else:
        cuerpo.pop()

    if ((posicion[0] < 0) or (posicion[0] >= Ancho) or (posicion[1] < 0) or (posicion[1] >= Largo)):
         print("Jugaste",str(round(time.time()-crono)),"segundos")
         break

#Cambia el color de la pantalla
    screen.fill(Verde)
    for body in cuerpo:
        pygame.draw.rect(screen,Gris,(body[0],body[1],15,15))
    pygame.draw.rect(screen,Rojo,(food[0],food[1],15,15))

    #Actualiza la pantalla
    pygame.display.flip()
    Fps.tick(10)
