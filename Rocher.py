
import random
import pygame
from pygame.math import Vector2


class Creep:
    def __init__(self):
        self.position = Vector2(random.randint(0,1400),random.randint(0,850))
        self.rayon = 5
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 10
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.l0 = 10
        self.k = 0.001
        self.vitessmin = 1
        self.maxVitesse = 4
        self.taillemax = 300
        self.freeze = False
        self.vivante = True
        self.maxAcceleration= 50


    def deplacement(self):
        if self.vivante:
            self.acceleration = Vector2(random.uniform(-1,1),random.uniform(-1,1))

            if self.acceleration.length() > self.maxAcceleration:
                self.acceleration.scale_to_length(self.maxAcceleration)

            self.vitesse = self.vitesse + self.acceleration

            if self.vitesse.length()>self.maxVitesse:
                self.vitesse.scale_to_length(self.maxVitesse)

            self.position = self.position + self.vitesse

            self.acceleration = Vector2(0,0)

    def bordure(self,fenetre):
        if self.position.y<0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y=0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0








    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)








        #random.randint(0,800).x,random.randint(0,800).y