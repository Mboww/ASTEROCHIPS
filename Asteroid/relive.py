import random

import pygame
from pygame import Vector2, image

import core




class Relive:
    def __init__(self,x=0,y=0, taille=30):  # à mettre à chaque fois pour définir les objets
        self.taille = 15
        self.position = Vector2()

    def show(self):
        core.Draw.circle((255,0,0),self.position,self.taille,0)


    def disparition(self, ship):
        dist = self.position.distance_to(ship.position)
        if dist < self.taille:
            return True
        return False
