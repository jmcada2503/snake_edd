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
Negro=(0,0,0)

#fps
Fps=pygame.time.Clock()

#ventana
screen= pygame.display.set_mode(size)

fuente= pygame.font.SysFont("arial",25)

#cordenadas
cord_x=Ancho//2
cord_y=Largo//2
#velocidad
velocidad=10

direccion=""
numero_de_fruta=0
#Funcion para la generacion de los puntos
def rand_food(num,cuerp):
        
        if num==0:
             #Esto es para la primera fruta
             posicion=[225,50]
        else:
            #Esto es paera generar las frutas aleatoriamente
            r1=random.randint(0,(Ancho//15))*15
            r2=random.randint(0,(Largo//15))*15
            a=True
            for body in cuerp:
                 #Esto es en caso de que la fruta se gener en el cuerpo de la serpiente
                 if body[0]!=r1 and body[1]!=r2:
                      a=True
                 else:
                      a=False
                      break
            if a==True:
                 posicion=[r1,r2]
            else:
                 posicion=rand_food(num,cuerp)
            
       
        return posicion

    


posicion = [cord_x, cord_y]
cuerpo = [[cord_x,cord_y],[cord_x,cord_y-15],[cord_x,cord_y-30]]
direccion = "u"
run = True
food = rand_food(numero_de_fruta,cuerpo)
numero_de_fruta=1
puntuacion = 0
crono=time.time()
while run==True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Esto es para quie imprima los segundo
                print("Jugaste",str(round(time.time()-crono)),"segundos")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key==pygame.K_w:
                    #Esto es para bloquear el movimiento
                    if direccion == "d":
                         pass
                    else:
                        direccion = 'u'
                if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                    if direccion == "u":
                         pass
                    else:
                        direccion = 'd'
                if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                    if direccion == "l":
                         pass
                    else:
                        direccion = 'r'
                if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                    if direccion == "r":
                         pass
                    else: 
                        direccion = 'l'
        
        
        if direccion == 'u':
            posicion[1] -= velocidad
        if direccion == 'd':
            posicion[1] += velocidad
        if direccion == 'r':
            posicion[0] += velocidad
        if direccion == 'l':
            posicion[0] -= velocidad

        cuerpo.insert(0, list(posicion))
        #El if esta entre < y < para que halla una area de acierto por asi decirlo, por que sino agarrar frutas es inexacto.

        if ((food[0]-10) <= posicion[0] <= (food[0]+10)) and ((food[1]-10) <= posicion[1] <= (food[1]+10)):
            food = rand_food(numero_de_fruta,cuerpo)
            puntuacion += 1
            print(puntuacion)

        else:
            cuerpo.pop()

        if ((posicion[0] < 0) or (posicion[0] > Ancho) or (posicion[1] < 0) or (posicion[1] > Largo)):
             print("Jugaste",str(round(time.time()-crono)),"segundos")
             break
             
       
        

   

    #Cambia el color de la pantalla
        screen.fill(Negro)   
        for body in cuerpo:
            #Aqui se imprime el cuerpo
            pygame.draw.rect(screen,Gris,(body[0],body[1],15,15))
        pygame.draw.rect(screen,Rojo,pygame.Rect(food[0],food[1],15,15))
        #Actualiza la pantalla
        pygame.display.flip()
        Fps.tick(10)
