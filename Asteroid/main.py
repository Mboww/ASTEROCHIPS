import time

import pygame
from pygame import Vector2
from pygame.rect import Rect
import core
from Asteroid import ship
from Asteroid.etat import Etat
from Asteroid.ship import Ship
from Asteroid.son import Son


def setup():
    # 1280, 720
    core.WINDOW_SIZE = [1280, 720]
    # core.memory("etat",Etat.MENU) <= initialisation
    core.fps = 60
    core.memory("etat", Etat.DEMARRAGE)
    Format = 0
    core.memory(("Vaisseau"),Ship())
    Son = True



def afficherDemarrage():
    Format = 1



    if core.getKeyPressList("") and Format!=0:
        Format = 0






    if Format == 1:

        #-------------Texte ASTEROID-------------------------------------------
        core.Draw.text((255, 255, 255), "ASTEROID", ((core.WINDOW_SIZE[0] / 2 - 280), (core.WINDOW_SIZE[1] / 2) - 250), 100, 'Doctor Glitch') #Arial #((core.WINDOW_SIZE[0] / 2 - 200), (core.WINDOW_SIZE[1] / 2) - 250), 100)
        #----------------------------------------------------------------------

        # -------------Texte PLAY-------------------------------------------
        #core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 125, (core.WINDOW_SIZE[1] / 2) - 50, 250, 100), 5)
        core.Draw.text((255, 255, 255), "PLAY", ((core.WINDOW_SIZE[0] / 2) - 110, (core.WINDOW_SIZE[1] / 2) - 40), 80, 'Doctor Glitch') #Arial #((core.WINDOW_SIZE[0] / 2) - 105, (core.WINDOW_SIZE[1] / 2) - 60), 105)

        Pos_SourisPlay = pygame.mouse.get_pos()
        recPlay = Rect((core.WINDOW_SIZE[0] / 2) - 125, (core.WINDOW_SIZE[1] / 2) - 50, 250, 100)

        if recPlay.collidepoint(Pos_SourisPlay):
            core.Draw.text((255, 255, 0), "PLAY", ((core.WINDOW_SIZE[0] / 2) - 110, (core.WINDOW_SIZE[1] / 2) - 40), 80,'Doctor Glitch')

            if core.getMouseLeftClick():
                Pos_SourisPlay = core.getMouseLeftClick()

                if recPlay.collidepoint(Pos_SourisPlay):
                    core.memory("etat", Etat.JEU)
    #----------------------------------------------------------------------


    # -------------Texte EXIT-------------------------------------------

        #core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 75, (core.WINDOW_SIZE[1] / 2) +80, 150, 80), 5)
        core.Draw.text((255, 255, 255), "EXIT", ((core.WINDOW_SIZE[0] / 2) - 65, (core.WINDOW_SIZE[1] / 2) + 92), 57, 'Doctor Glitch') #Arial #((core.WINDOW_SIZE[0] / 2) - 65, (core.WINDOW_SIZE[1] / 2) + 80), 70)

        Pos_SourisExit = pygame.mouse.get_pos()
        recExit = Rect((core.WINDOW_SIZE[0] / 2) - 75, (core.WINDOW_SIZE[1] / 2) +80, 150, 80)

        if recExit.collidepoint(Pos_SourisExit):
            core.Draw.text((255, 255, 0), "EXIT", ((core.WINDOW_SIZE[0] / 2) - 65, (core.WINDOW_SIZE[1] / 2) + 92), 57, 'Doctor Glitch')

            if core.getMouseLeftClick():
                Pos_SourisExit = core.getMouseLeftClick()

                if recExit.collidepoint(Pos_SourisExit):
                    time.sleep(0.1)
                    exit()

    # ----------------------------------------------------------------------


    # -------------Texte Crédit-------------------------------------------

        core.Draw.text((255, 255, 255), "Credit", (20, (core.WINDOW_SIZE[1] / 2) + 320), 20, 'Doctor Glitch')
        #core.Draw.rect((255, 255, 255), (20, (core.WINDOW_SIZE[1] / 2) + 318, 85, 25), 2)
        Pos_SourisCredit = pygame.mouse.get_pos()
        recCredit = Rect(20, (core.WINDOW_SIZE[1] / 2) + 318, 85, 25)

        if recCredit.collidepoint(Pos_SourisCredit):
            core.Draw.text((255, 255, 0), "Credit", (20, (core.WINDOW_SIZE[1] / 2) + 320), 20, 'Doctor Glitch')


            if core.getMouseLeftClick():
                Pos_SourisCredit = core.getMouseLeftClick()

                if recCredit.collidepoint(Pos_SourisCredit):
                    core.memory("etat", Etat.CREDIT)


    #----------------------------------------------------------------------
    else:
    #-------------Texte ASTEROID-------------------------------------------
        core.Draw.text((255, 255, 255), "ASTEROID", ((core.WINDOW_SIZE[0] / 2 - 180), (core.WINDOW_SIZE[1] / 2) - 220), 100,'')  # Arial #((core.WINDOW_SIZE[0] / 2 - 200), (core.WINDOW_SIZE[1] / 2) - 250), 100)
    # ----------------------------------------------------------------------

    # -------------Texte PLAY-------------------------------------------
        #core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 100, (core.WINDOW_SIZE[1] / 2) - 62, 198, 70), 5)
        core.Draw.text((255, 255, 255), "PLAY", ((core.WINDOW_SIZE[0] / 2) - 95, (core.WINDOW_SIZE[1] / 2) - 60), 105,'')  # Arial #((core.WINDOW_SIZE[0] / 2) - 105, (core.WINDOW_SIZE[1] / 2) - 60), 105)

        Pos_SourisPlay = pygame.mouse.get_pos()
        recPlay = Rect((core.WINDOW_SIZE[0] / 2) - 100, (core.WINDOW_SIZE[1] / 2) - 62, 198, 70)

        if recPlay.collidepoint(Pos_SourisPlay):
            core.Draw.text((255, 255, 0), "PLAY", ((core.WINDOW_SIZE[0] / 2) - 95, (core.WINDOW_SIZE[1] / 2) - 60), 105,'')

            if core.getMouseLeftClick():
                Pos_SourisPlay = core.getMouseLeftClick()

                if recPlay.collidepoint(Pos_SourisPlay):
                    core.memory("etat", Etat.JEU)
    # ----------------------------------------------------------------------

    # -------------Texte EXIT-------------------------------------------

        #core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 75, (core.WINDOW_SIZE[1] / 2) + 85, 135, 55), 5)
        core.Draw.text((255, 255, 255), "EXIT", ((core.WINDOW_SIZE[0] / 2) - 68, (core.WINDOW_SIZE[1] / 2) + 90), 70,'')  # Arial #((core.WINDOW_SIZE[0] / 2) - 65, (core.WINDOW_SIZE[1] / 2) + 80), 70)

        Pos_SourisExit = pygame.mouse.get_pos()
        recExit = Rect((core.WINDOW_SIZE[0] / 2) - 75, (core.WINDOW_SIZE[1] / 2) + 85, 135, 55)

        if recExit.collidepoint(Pos_SourisExit):
            core.Draw.text((255, 255, 0), "EXIT", ((core.WINDOW_SIZE[0] / 2) - 68, (core.WINDOW_SIZE[1] / 2) + 90), 70,'')

            if core.getMouseLeftClick():
                Pos_SourisExit = core.getMouseLeftClick()

                if recExit.collidepoint(Pos_SourisExit):
                    time.sleep(0.1)
                    exit()

    # ----------------------------------------------------------------------

    # -------------Texte Crédit-------------------------------------------

        core.Draw.text((255, 255, 255), "Credit", (20, (core.WINDOW_SIZE[1] / 2) + 320), 40, '')
        #core.Draw.rect((255, 255, 255), (18, (core.WINDOW_SIZE[1] / 2) + 318, 88, 28), 2)
        Pos_SourisCredit = pygame.mouse.get_pos()
        recCredit = Rect(18, (core.WINDOW_SIZE[1] / 2) + 318, 88, 28)

        if recCredit.collidepoint(Pos_SourisCredit):
            core.Draw.text((255, 255, 0), "Credit", (20, (core.WINDOW_SIZE[1] / 2) + 320), 40, '')

            if core.getMouseLeftClick():
                Pos_SourisCredit = core.getMouseLeftClick()

                if recCredit.collidepoint(Pos_SourisCredit):
                    core.memory("etat", Etat.CREDIT)

    # ----------------------------------------------------------------------









    # -------------SonOn/Off-------------------------------------------

    if Son == True:


        if not core.memory("SonOn").ready:
            core.memory("SonOn").load()
    core.memory("SonOn", core.Texture("./SoundOn.png", Vector2(1210, (core.WINDOW_SIZE[1] / 2) + 290), 0, [50, 50]))
    core.memory("SonOn").show()


    #----------------------------------------------------------------------











   #if core.getMouseLeftClick():
   #     position = core.getMouseLeftClick()
   #     rec = Rect(380, 280, 90, 40)
   #
   #     if rec.collidepoint(position):
   #         core.memory("etat", Etat.JEU)




def afficherJeu():
    core.memory('Vaisseau').show()



def afficherGameOver():
    core.Draw.text((255, 255, 255), "GAMEOVER", (365, 280), 30)


def afficherMenu():
    pass


def afficherCredit():
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


