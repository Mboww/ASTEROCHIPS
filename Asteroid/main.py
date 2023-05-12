import time
from random import random

import pygame
from pygame import Vector2
from pygame.rect import Rect
import core
from Asteroid import ship
from Asteroid.asteroide import Asteroide
from Asteroid.etat import Etat
from Asteroid.map import Map
from Asteroid.projectil import Projectile
from Asteroid.ship import Ship
#from Asteroid.son import Son


def setup():
    # 1280, 720
    core.WINDOW_SIZE = [1280, 720]
    # core.memory("etat",Etat.MENU) <= initialisation
    core.fps = 60
    core.memory("etat", Etat.DEMARRAGE)
    Format = 0
    core.memory(("Vaisseau"),Ship())
    core.memory(("Asteroide"), Asteroide())
    core.memory(("Map"), Map())


    core.memory("SonOn", core.Texture("./Asset/SoundOn.png", Vector2(1210, (core.WINDOW_SIZE[1] / 2) + 290), 0, [50, 50]))
    core.memory("SonOff", core.Texture("./Asset/SoundOff.png", Vector2(1210, (core.WINDOW_SIZE[1] / 2) + 290), 0, [50, 50]))
    core.memory("Son", 1)
    core.memory("Regles",core.Texture("./Asset/Regles.png", Vector2(-60, 0), 0, [1400, 787]))
    core.memory("ReglesOK",0)
    core.memory("Info", core.Texture("./Asset/Info.png", Vector2(1210, 20), 0, [60, 60]))

    core.memory("mesProjectiles", [])

def creationProjectile():
    proj = Projectile()
    proj.position = Vector2(core.memory('Vaisseau').Pos) + 35*core.memory('Vaisseau').orientation
    proj.acceleration = Vector2(core.memory('Vaisseau').orientation)
    #proj.acceleration = Vector2(0,-1)
    core.memory('mesProjectiles').append(proj)


def afficherDemarrage():

    # -------------Texte ASTEROID-------------------------------------------
    core.Draw.text((255, 255, 255), "ASTEROID", ((core.WINDOW_SIZE[0] / 2 - 280), (core.WINDOW_SIZE[1] / 2) - 250), 100,
                   'Doctor Glitch')  # Arial #((core.WINDOW_SIZE[0] / 2 - 200), (core.WINDOW_SIZE[1] / 2) - 250), 100)
    # ----------------------------------------------------------------------


    # -------------Texte PLAY/EXIT/CREDIT-------------------------------------------
    # core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 100, (core.WINDOW_SIZE[1] / 2) - 62, 198, 70), 5)
    core.Draw.text((255, 255, 255), "PLAY", ((core.WINDOW_SIZE[0] / 2) - 95, (core.WINDOW_SIZE[1] / 2) - 60), 105,
                   '')  # Arial #((core.WINDOW_SIZE[0] / 2) - 105, (core.WINDOW_SIZE[1] / 2) - 60), 105)

    Pos_SourisPlay = pygame.mouse.get_pos()
    recPlay = Rect((core.WINDOW_SIZE[0] / 2) - 100, (core.WINDOW_SIZE[1] / 2) - 62, 198, 70)

    if recPlay.collidepoint(Pos_SourisPlay) and core.memory("ReglesOK") == 0:
        core.Draw.text((255, 255, 0), "PLAY", ((core.WINDOW_SIZE[0] / 2) - 95, (core.WINDOW_SIZE[1] / 2) - 60), 105, '')

        if core.getMouseLeftClick():
            Pos_SourisPlay = core.getMouseLeftClick()

            if recPlay.collidepoint(Pos_SourisPlay):
                core.memory("etat", Etat.JEU)
    # ----------------------------------------------------------------------

    # -------------Texte EXIT-------------------------------------------

    # core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 75, (core.WINDOW_SIZE[1] / 2) + 85, 135, 55), 5)
    core.Draw.text((255, 255, 255), "EXIT", ((core.WINDOW_SIZE[0] / 2) - 68, (core.WINDOW_SIZE[1] / 2) + 90), 70,
                   '')  # Arial #((core.WINDOW_SIZE[0] / 2) - 65, (core.WINDOW_SIZE[1] / 2) + 80), 70)

    Pos_SourisExit = pygame.mouse.get_pos()
    recExit = Rect((core.WINDOW_SIZE[0] / 2) - 75, (core.WINDOW_SIZE[1] / 2) + 85, 135, 55)

    if recExit.collidepoint(Pos_SourisExit) and core.memory("ReglesOK") == 0:
        core.Draw.text((255, 255, 0), "EXIT", ((core.WINDOW_SIZE[0] / 2) - 68, (core.WINDOW_SIZE[1] / 2) + 90), 70, '')

        if core.getMouseLeftClick():
            Pos_SourisExit = core.getMouseLeftClick()

            if recExit.collidepoint(Pos_SourisExit):
                time.sleep(0.1)
                exit()

    # ----------------------------------------------------------------------

    # -------------Texte Crédit-------------------------------------------

    core.Draw.text((255, 255, 255), "Credit", (20, (core.WINDOW_SIZE[1] / 2) + 320), 40, '')
    # core.Draw.rect((255, 255, 255), (18, (core.WINDOW_SIZE[1] / 2) + 318, 88, 28), 2)
    Pos_SourisCredit = pygame.mouse.get_pos()
    recCredit = Rect(18, (core.WINDOW_SIZE[1] / 2) + 318, 88, 28)

    if recCredit.collidepoint(Pos_SourisCredit) and core.memory("ReglesOK") == 0:
        core.Draw.text((255, 255, 0), "Credit", (20, (core.WINDOW_SIZE[1] / 2) + 320), 40, '')

        if core.getMouseLeftClick():
            Pos_SourisCredit = core.getMouseLeftClick()

            if recCredit.collidepoint(Pos_SourisCredit):
                core.memory("etat", Etat.CREDIT)

            # ---------------------------

    # -------------SON------------------------------------------------
    # if Son == True:

    #core.Draw.rect((255, 255, 255), (1210, (core.WINDOW_SIZE[1] / 2) + 290, 50, 50), 5)
    Pos_SourisSon = pygame.mouse.get_pos()
    recSon = Rect((1210, (core.WINDOW_SIZE[1] / 2) + 290, 50, 50))

    if not core.memory("SonOn").ready:
        core.memory("SonOn").load()
    if not core.memory("SonOff").ready:
        core.memory("SonOff").load()

    if recSon.collidepoint(Pos_SourisSon):

        if core.getMouseLeftClick():
            Pos_SourisSon = core.getMouseLeftClick()
            time.sleep(0.5)

            if recSon.collidepoint(Pos_SourisSon):
                if core.memory("Son") == 0:
                    core.memory("Son", 1)
                elif core.memory("Son") == 1:
                    core.memory("Son", 0)

    if core.memory("Son") == 0:
        core.memory("SonOff").load()
        core.memory("SonOff").show()



    if core.memory("Son") == 1:
        core.memory("SonOn").load()
        core.memory("SonOn").show()



    core.cleanScreen()



    # ----------------------------------------------------------------------


    if core.memory("ReglesOK") == 1:

        if core.getMouseLeftClick() or core.getMouseRightClick():
            core.memory("ReglesOK",0)

        if not core.memory("Regles").ready:
            core.memory("Regles").load()

        core.memory("Regles").show()
        core.cleanScreen()

        if core.memory("ReglesOK") == 0:
            time.sleep(0.4)

    if not core.memory("Info").ready:
        core.memory("Info").load()
    core.memory("Info").show()

    #core.Draw.rect((255, 255, 255), (1220, 18, 40, 65), 5)
    Pos_SourisInfo = pygame.mouse.get_pos()
    recInfo = Rect(1220, 18, 40, 65)


    if core.getMouseLeftClick():
        Pos_SourisInfo = core.getMouseLeftClick()

        if recInfo.collidepoint(Pos_SourisInfo):
            core.memory("ReglesOK", 1)





def afficherJeu():

    if core.getKeyPressList("ESCAPE"):
        core.memory("etat", Etat.DEMARRAGE)

    core.memory('Vaisseau').deplacement()
    core.memory('Vaisseau').show()
    core.memory('Map').spawnAst()

    if core.getKeyPressList("SPACE"):
        print("yes")
        if len(core.memory('mesProjectiles'))>0:
            if time.time() - core.memory('mesProjectiles')[-1].startTime >0.2:
                creationProjectile()

        else:
            creationProjectile()


    for p in core.memory('mesProjectiles'):
        if time.time() - p.startTime > p.dureedevie :
            core.memory('mesProjectiles').remove(p)

    for p in core.memory('mesProjectiles'):
        p.deplacement()
        p.draw()


def afficherGameOver():
    core.Draw.text((255, 255, 255), "GAMEOVER", (365, 280), 30)
    if core.getKeyPressList("ESCAPE"):
        core.memory("etat", Etat.DEMARRAGE)


def afficherMenu():
    #if core.getKeyPressList("ESCAPE"):
    #    core.memory("etat", Etat.DEMARRAGE)
    pass


def afficherCredit():

    if core.getKeyPressList("ESCAPE"):
        core.memory("etat", Etat.DEMARRAGE)












def run():
    core.cleanScreen()
    if core.memory('etat') == Etat.DEMARRAGE:
        afficherDemarrage()

    if core.memory('etat') == Etat.JEU:
        afficherJeu()

    if core.memory('etat') == Etat.GAMEOVER:
        afficherGameOver()

    if core.memory('etat') == Etat.MENU:
        afficherMenu()

    if core.memory('etat') == Etat.CREDIT:
        afficherCredit()


core.main(setup, run)


