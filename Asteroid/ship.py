from pygame import Vector2

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
        self.Taille = 5

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
        #if core.getkeyPressList("z"):
        pass


    def collision(self):
        pass


    def show(self):
        core.Draw.circle((255,255,255),self.Pos,self.Taille)


