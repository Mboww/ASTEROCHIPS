from pygame import Vector2

import core


class Map:
    def __init__(self):
        self.taille = Vector2(core.WINDOW_SIZE[0],core.WINDOW_SIZE[1])
        self.MaxAst = 8
        self.MaxEnemy = 2
        self.zonespawn = Vector2
        self.zoneteleportatin= Vector2



    def spawnAst(self):

        #core.Draw.rect((255,255,255),(core.WINDOW_SIZE[0] , core.WINDOW_SIZE[1] - 100))


        #if recExit.collidepoint(Pos_SourisExit):
        #    core.Draw.text((255, 255, 0), "EXIT", ((core.WINDOW_SIZE[0] / 2) - 68, (core.WINDOW_SIZE[1] / 2) + 90), 70,'')
        pass

    def spawnEnemy(self):
        pass