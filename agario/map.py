from pygame import Vector2

import core


class Map:
    def __init__(self):
        self.maxPlayer = 20
        self.maxFood = 100
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueurs = []  # [vide] pour faire une liste si y'en a plusieurs
        self.food = []
        self.pieges = []

    def spawn_food(self):
        pass

    def spawn_player(self):
        pass

    def show(self):
        for j in self.joueurs:
            # itérateur prend les éléments du tableau l'un après l'autre jusqu'à qu'il n'y ai plus rien dedans
            j.show()

    def addJoueur(self, p):
        if len(self.joueurs) < self.maxPlayer:
            self.joueurs.append(p)  # .append=ajout de ce q'il ya dans la parenthèse
