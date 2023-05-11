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
        self.Taille = 50
        self.orientation = Vector2(0, -1)

    #def deplacement(self):  # création des méthodes
        #if core.getKeyPressList("d"):
           # k = 0.01
           # u = 1
            #l = (self.Pos - 4)
            #l0 = 0.001
            #Fa = (k * u * (l - l0))
            #self.acc = Fa
        #self.vitesse = self.vitesse + self.acc
        #self.position = self.position + self.vitesse

    def deplacement(self):

        if core.getKeyPressList("z"):  # déplacement vers le haut
            self.Acc = Vector2(self.orientation)
            self.Vitesse += self.Acc
            self.Pos += self.orientation

        if core.getKeyPressList("d"): #rotation sens horaire
            self.orientation = self.orientation.rotate(2)

        if core.getKeyPressList("q"): #rotation sens non-horaire
            self.orientation = self.orientation.rotate(-2)

    def collision(self):
        pass


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

        core.Draw.polygon((255,255,255),((p1),(p2),(p3)),1) #création d'un triangle