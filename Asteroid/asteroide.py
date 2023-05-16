import random

import pygame
from pygame import Vector2, image

import core


class Asteroide:
    def __init__(self,x=0,y=0, taille=30):  # à mettre à chaque fois pour définir les objets
        pygame.display.set_mode((1280,720))
        self.taille = 30
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.Vmax = 2
        self.Accmax = 2
        self.position = Vector2(x,y)
        self.skin = pygame.image.load("./Asset/ASTEROID.png").convert_alpha()
        self.skin = pygame.transform.scale(self.skin, (self.taille, self.taille))
        self.rect = self.skin.get_rect(center=(x, y))

    def deplacement(self):
        if self.acc.length() > self.Accmax:
            self.acc.scale_to_length(self.Accmax)

        if self.vitesse.length() > self.Vmax:
            self.vitesse.scale_to_length(self.Vmax)

        self.vitesse += self.acc
        self.position += self.vitesse

    def show(self):
        #core.Draw.circle((255,255,255),self.position,self.taille,5)
        self.rect.center = (self.position.x, self.position.y)
        pygame.display.get_surface().blit(self.skin, self.rect)

        #core.Draw.rect((100,0,120),(self.position.x-15, self.position.y-15,30,30))



    def teleportation(self):
        if self.position.x < 0: #sortie gauche
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x > core.WINDOW_SIZE[0]: #sortie droite
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = 0

    def collision(self, projectile):
        dist = self.position.distance_to(projectile.position)
        if dist < self.taille:
            return True
        return False

    def destruction(self, vaisseau):
        dist = self.position.distance_to(vaisseau.Pos)
        if dist < self.taille:
            return True
        return False

asteroideGrand = Asteroide(x=100, y=100, taille=30)
asteroideMoyen = Asteroide(x=200, y=200, taille=50)
asteroidePetit = Asteroide(x=300, y=300, taille=80)
