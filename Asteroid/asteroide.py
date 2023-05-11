from pygame import Vector2

import core


class Asteroide:
    def __init__(self):  # à mettre à chaque fois pour définir les objets
        self.taille = 5
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.Vmax = 10
        self.Accmax = 10

    def deplacement(self):
        pass

    #def show(self):
        #core.Draw.circle((255,255,255),)
