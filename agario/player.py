import random

from pygame import Vector2

import core


class Player:
    def __init__(self):  # à mettre à chaque fois pour définir les objets
        self.bot = True
        self.name = "Alice"  # "" chaine de caractères
        self.uuid = random.randint(1000000, 9999999999)  # random à importer
        self.mass = 10
        self.vMax = 10
        self.accMax = 5
        self.acc = Vector2(0, 0)
        self.vitesse = Vector2(0, 0)
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        # x et y du vecteur #WINDOW_SIZE est un tableau. On ne veut pas tout le tableau, on veut que une certaine
        # position [0] récupère l'argument 0 dans le tableau
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def deplacement(self):  # création des méthodes
        if self.bot == False:
            if core.getMouseLeftClick():
                k = 0.01
                u = 1
                l = (self.position - core.getMouseLeftClick())
                l0 = 0.001
                Fa = (k * u * (l - l0))
                self.acc = Fa
            self.vitesse = self.vitesse + self.acc
            self.position = self.position + self.vitesse

    def grandir(self):
        pass

    def evaporation(self):
        pass

    def show(self):
        core.Draw.circle(self.couleur, self.position, self.mass)
