import time

from pygame import Vector2
from pygame.draw import polygon

import core


class Ship:
    def __init__(self):
        self.Pos = Vector2((core.WINDOW_SIZE[0]/2),(core.WINDOW_SIZE[1]/2))
        self.Vitesse = Vector2(0, 0)
        self.Acc = Vector2(0, 0)
        self.VitesseMax = 10
        self.AccMax = 10
        self.NbrVie = 3
        self.Mass = 1

        self.orientation = Vector2(0, -1)


    def deplacement(self):

        if core.getKeyPressList("z"):  # déplacement vers le haut
            self.Acc = Vector2(self.orientation)
            self.Vitesse += self.Acc
            self.Pos += self.orientation

        if core.getKeyPressList("d"): #rotation sens horaire
            self.orientation = self.orientation.rotate(3)


        if core.getKeyPressList("q"): #rotation sens non-horaire
            self.orientation = self.orientation.rotate(-3)

        self.Pos += self.Acc
        self.Acc = self.Acc*0.995

        if self.Acc.length() < 0.25:
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
        core.Draw.circle((0, 0, 255), hauteur, 18, 1)
        core.Draw.polygon((255,255,255),((p1),(p2),(p3)),1)



    def teleportation(self):
        if self.Pos.x < 0: #sortie gauche
            self.Pos.x = core.WINDOW_SIZE[0]
        if self.Pos.x > core.WINDOW_SIZE[0]: #sortie droite
            self.Pos.x = 0

        if self.Pos.y < 0:
            self.Pos.y = core.WINDOW_SIZE[1]
        if self.Pos.y > core.WINDOW_SIZE[1]:
            self.Pos.y = 0