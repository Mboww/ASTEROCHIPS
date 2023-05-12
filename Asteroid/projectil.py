import time

from pygame import Vector2

import core
from Asteroid.ship import Ship


class Projectile:
    def __init__(self):
        self.taille = 5
        self.vitesse= Vector2(0,0)
        self.acceleration = Vector2(0,0)
        self.position = Vector2()
        self.dureedevie = 3
        self.startTime = time.time()
        self.orientation = Vector2(0, -1)
        self.ship = Ship()

    def deplacement(self):

        self.vitesse += self.acceleration
        #self.position = Vector2(self.ship.Pos)
        self.position += self.vitesse

        pass

    def collision(self):

        pass

    def draw(self):
        core.Draw.circle((255,255,255), self.position, self.taille)