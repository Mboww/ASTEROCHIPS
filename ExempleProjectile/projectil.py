import time
from random import random

from pygame import Vector2

import core


class Projectile:
    def __init__(self):
        self.taille = 5
        self.vitesse= Vector2()
        self.acceleration = Vector2()
        self.position = Vector2()
        self.dureedevie = 3
        self.startTime = time.time()

    def deplacement(self):
        self.vitesse+=self.acceleration
        self.position += self.vitesse

    def collition(self):
        pass

    def draw(self):
        core.Draw.circle((255,255,255),self.position,self.taille)

    def creationProjectile(position):
        proj = Projectile()
        proj.position = Vector2(position)
        proj.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        core.memory('mesProjectiles').append(proj)