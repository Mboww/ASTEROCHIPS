import time

import pygame
from pygame import Vector2
from pygame.draw import polygon

import core



class Ship:
    def __init__(self,x=0,y=0):

        self.taille = 30
        self.Pos = Vector2((core.WINDOW_SIZE[0]/2),(core.WINDOW_SIZE[1]/2))
        self.Vitesse = Vector2(0, 0)
        self.Acc = Vector2(0, 0)
        self.VitesseMax = 2
        self.AccMax = 3
        self.NbrVie = 3
        self.Mass = 1
        self.orientation = Vector2(0, -1)
        self.name = "monvaisseau"
        self.length = 10
        self.position = Vector2(x, y)



    def deplacement(self):

        if core.getKeyPressList("z"):  # déplacement vers le haut
            self.Acc = Vector2(self.orientation)
            self.Vitesse += self.Acc
            #self.Pos += self.orientation
            self.Pos += self.Vitesse

            if self.Acc.length() > self.AccMax:
                self.Acc.scale_to_length(self.AccMax)

            if self.Vitesse.length() > self.VitesseMax:
                self.Vitesse.scale_to_length(self.VitesseMax)

        if core.getKeyPressList("d"): #rotation sens horaire
            self.orientation = self.orientation.rotate(3)


        if core.getKeyPressList("q"): #rotation sens non-horaire
            self.orientation = self.orientation.rotate(-3)

        self.Vitesse = self.Vitesse*0.99
        self.Pos += self.Vitesse


        if self.Acc.length() < 1.5:
            self.Acc = Vector2(0, 0)



    def show(self):

        p1 = self.orientation.rotate(90) #Point1 du triangle
        p1.scale_to_length(20)
        p1 = p1 + self.Pos

        p3 = self.orientation.rotate(-90) #Point3 du triangle
        p3.scale_to_length(20)
        p3 = p3 + self.Pos

        p2 = Vector2(self.orientation) #Point2 du triangle
        p2.scale_to_length(40)
        p2 = p2 + self.Pos

        #création d'un triangle
        hauteur = Vector2(self.orientation)
        hauteur.scale_to_length(40/3)
        hauteur = hauteur + self.Pos
        #core.Draw.circle((0, 0, 255), hauteur, 19)
        core.Draw.polygon((255,255,255),((p1),(p2),(p3)),2)

        #pygame.display.set_mode((1280, 720))
        #self.skin = pygame.image.load("./Asset/Ship.png").convert_alpha()
        #self.skin = pygame.transform.scale(self.skin, (self.taille, self.taille))
        #self.rect = self.skin.get_rect(center=(x, y))

    def teleportation(self):
        if self.Pos.x < 0: #sortie gauche
            self.Pos.x = core.WINDOW_SIZE[0]
        if self.Pos.x > core.WINDOW_SIZE[0]: #sortie droite
            self.Pos.x = 0

        if self.Pos.y < 0:
            self.Pos.y = core.WINDOW_SIZE[1]
        if self.Pos.y > core.WINDOW_SIZE[1]:
            self.Pos.y = 0