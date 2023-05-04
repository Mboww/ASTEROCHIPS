from pygame.rect import Rect
import core
from Asteroid.etat import Etat


def setup():
    # 1220,720
    core.WINDOW_SIZE = [1220, 720]
    # core.memory("etat",Etat.MENU) <= initialisation
    core.fps = 60
    core.memory("etat", Etat.DEMARRAGE)
    print("end setup")



def afficherDemarrage():
    #-------------Texte ASTEROID
    core.Draw.text((255, 255, 255), "ASTEROID", ((core.WINDOW_SIZE[0] / 2 - 200), (core.WINDOW_SIZE[1] / 2) - 250), 100)
    #-------------

    # -------------Texte PLAY
    core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 125, (core.WINDOW_SIZE[1] / 2) - 50, 250, 100), 5)
    core.Draw.text((255, 255, 255), "PLAY", ((core.WINDOW_SIZE[0] / 2) - 105, (core.WINDOW_SIZE[1] / 2) - 60), 105)

    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect((core.WINDOW_SIZE[0] / 2) - 125, (core.WINDOW_SIZE[1] / 2) - 50, 250, 100)

        if rec.collidepoint(position):
            core.memory("etat", Etat.JEU)
    # -------------


    # -------------Texte EXIT
    core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 75, (core.WINDOW_SIZE[1] / 2) +80, 150, 80), 5)
    core.Draw.text((255, 255, 255), "EXIT", ((core.WINDOW_SIZE[0] / 2) - 65, (core.WINDOW_SIZE[1] / 2) + 80), 70)

    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect((core.WINDOW_SIZE[0] / 2) - 75, (core.WINDOW_SIZE[1] / 2) +80, 150, 80)

        #if rec.collidepoint(position):
            #code fermeture prog (altf4)
    # -------------


    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect(380, 280, 90, 40)

        if rec.collidepoint(position):
            core.memory("etat", Etat.JEU)


def afficherJeu():
    # print("Jeu")
    pass


def afficherGameOver():
    core.Draw.text((255, 255, 255), "GAMEOVER", (365, 280), 30)


def afficherMenu():
    pass


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


core.main(setup, run)
