import random
import time

from pygame import Vector2

import core
from ExempleProjectile.projectil import Projectile


def setup():
    core.WINDOW_SIZE=[1280,720]
    core.fps = 30
    core.memory("mesProjectiles", [])

def creationProjectile(position):
    proj = Projectile()
    proj.position = Vector2(position)
    proj.acceleration = Vector2(random.uniform(-1,1),random.uniform(-1,1))
    core.memory('mesProjectiles').append(proj)

def run():
    core.cleanScreen()
    if core.getMouseLeftClick():
        if len(core.memory('mesProjectiles'))>0:
            if time.time() - core.memory('mesProjectiles')[-1].startTime >0.2:
                creationProjectile(core.getMouseLeftClick())
        else:
            creationProjectile(core.getMouseLeftClick())

    for p in core.memory('mesProjectiles'):
        if time.time() - p.startTime > p.dureedevie :
            core.memory('mesProjectiles').remove(p)

    for p in core.memory('mesProjectiles'):
        p.deplacement()
        p.draw()


core.main(setup,run)

