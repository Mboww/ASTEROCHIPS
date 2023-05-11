from pygame import Vector2

import core


class Map:
    def __init__(self):
        self.taille = Vector2(core.WINDOW_SIZE)
        self.MaxAst = 8
        self.MaxEnemy = 2
        self.zonespawn = Vector2
        self.zonetel= Vector2

    def spawnAst(self):

        core.Draw.rect((0,0,255),(0, 0,10,720))
        core.Draw.rect((0, 0, 255), (0, 0, 1280, 10))
        core.Draw.rect((0, 0, 255), (1270, 0, 10, 720))
        core.Draw.rect((0, 0, 255), (0, 710, 1280, 10))
        if

    def spawnEnemy(self):
        pass