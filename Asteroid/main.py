import random
import time

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


# from Asteroid.son import Son

#FAIRE ANNEE DANS CREDIT, logo ecole why not ? , linkedin, asté en icon, install police



def setup():
    # 1280, 720
    core.WINDOW_SIZE = [1280, 720]
    # core.memory("etat",Etat.MENU) <= initialisation
    core.fps = 60
    # core.memory("etat", Etat.DEMARRAGE)
    core.memory("etat", Etat(0))

    Format = 0
    v=Ship()
    core.memory(("Vaisseau"), v)

    core.memory(("Asteroide"), Asteroide())
    core.memory(("Map"), Map())

    core.memory("SonOn",
                core.Texture("./Asset/SoundOn.png", Vector2(1210, (core.WINDOW_SIZE[1] / 2) + 290), 0, [50, 50]))
    core.memory("SonOff",
                core.Texture("./Asset/SoundOff.png", Vector2(1210, (core.WINDOW_SIZE[1] / 2) + 290), 0, [50, 50]))
    core.memory("Son", 1)
    core.memory("Regles", core.Texture("./Asset/Regles.png", Vector2(-60, 0), 0, [1400, 787]))
    core.memory("ReglesOK", 1)
    core.memory("Info", core.Texture("./Asset/Info.png", Vector2(1210, 20), 0, [60, 60]))
    core.memory("Vie3", core.Texture("./Asset/Vie.png", Vector2(1100, 10),0,[60, 60]))
    core.memory("Vie2", core.Texture("./Asset/Vie.png", Vector2(1155, 10), 0, [60, 60]))
    core.memory("Vie1", core.Texture("./Asset/Vie.png", Vector2(1210, 10), 0, [60, 60]))
    core.memory("Credit", core.Texture("./Asset/Credit.png", Vector2(0, 0), 0, [1280, 720]))
    #core.memory("IMGAst", core.Texture("./Asset/ASTEROID.png",Vector2(0, 0), 0, [1280, 720]))
    core.memory("mesProjectiles", [])
    core.memory("mesAsteroides", [])
    #core.memory('monVaisseau',[v])
    core.memory('VieV',3)
    core.memory('total',0)
    ecran = pygame.display.set_mode((core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))


    for i in range(0, 3):
        position_x = random.randint(0, core.WINDOW_SIZE[0])
        position_y = random.randint(-10, 10)
        creationAsteroide(position_x, position_y,60)



def creationProjectile():
    proj = Projectile()
    proj.position = Vector2(core.memory('Vaisseau').Pos) + 35 * core.memory('Vaisseau').orientation
    proj.acceleration = Vector2(core.memory('Vaisseau').orientation)
    core.memory('mesProjectiles').append(proj)


def creationAsteroide(position_x, position_y,taille):
    ast = Asteroide()
    ast.position = Vector2(position_x, position_y)
    ast.acc = Vector2((random.uniform(-1, 1)), random.uniform(-1, 1))
    ast.taille = taille
    core.memory('mesAsteroides').append(ast)


def afficherDemarrage():

    core.memory('total', 0)

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

    # core.Draw.rect((255, 255, 255), (1210, (core.WINDOW_SIZE[1] / 2) + 290, 50, 50), 5)
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
        core.memory("SonOff").show()

    if core.memory("Son") == 1:
        core.memory("SonOn").show()

    core.cleanScreen()

    # ----------------------------------------------------------------------
    if not core.memory("Info").ready:
        core.memory("Info").load()
    core.memory("Info").show()




    if core.memory("ReglesOK") == 1:



        if core.getMouseLeftClick() or core.getMouseRightClick() or core.getKeyPressList("ESCAPE"):
            core.memory("ReglesOK", 0)


        if not core.memory("Regles").ready:
            core.memory("Regles").load()

        core.memory("Regles").show()


        if core.memory("ReglesOK") == 0:
            time.sleep(0.4)



    # core.Draw.rect((255, 255, 255), (1220, 18, 40, 65), 5)
    Pos_SourisInfo = pygame.mouse.get_pos()
    recInfo = Rect(1220, 18, 40, 65)

    if core.getMouseLeftClick():
        Pos_SourisInfo = core.getMouseLeftClick()

        if recInfo.collidepoint(Pos_SourisInfo):
            core.memory("ReglesOK", 1)


    core.cleanScreen()


def afficherJeu():



    #ecran = pygame.display.set_mode((core.WINDOW_SIZE))
    if core.getKeyPressList("p"):
        core.memory("etat", Etat.MENU)

    #affichage zone
    core.memory('Map').spawnAst()

    core.memory('Vaisseau').deplacement()
    core.memory('Vaisseau').show()
    core.memory('Vaisseau').teleportation()


#lancer projectiles
    if core.getKeyPressList("SPACE"):
        if len(core.memory('mesProjectiles')) > 0:
            if time.time() - core.memory('mesProjectiles')[-1].startTime > 0.2:
                creationProjectile()
        else:
            creationProjectile()

    for p in core.memory('mesProjectiles'):
        if time.time() - p.startTime > p.dureedevie:
            core.memory('mesProjectiles').remove(p)

    for p in core.memory('mesProjectiles'):
        p.deplacement()
        p.draw()

# spawn asteroide
    for a in core.memory('mesAsteroides'):
        a.show()
        a.deplacement()
        a.teleportation()

#collision asteroide + calcul score



    Tt=(core.memory('total'))
    for a in core.memory('mesAsteroides'):
        for p in core.memory('mesProjectiles'):
            result = a.collision(p)
            if result:
                if a.taille > 15:
                    creationAsteroide(p.position.x,p.position.y,a.taille/2)
                    creationAsteroide(p.position.x, p.position.y, a.taille/2)
                    Tt += 20
                else :
                    Tt += 50
                core.memory('mesProjectiles').remove(p)
                core.memory('mesAsteroides').remove(a)
                core.memory('total',Tt)



#collision vaisseau
    for a in core.memory('mesAsteroides'):
        result = a.destruction(core.memory("Vaisseau"))
        if result:
            core.memory("Vaisseau").NbrVie -= 1
            core.memory("Vaisseau").Pos = Vector2((core.WINDOW_SIZE[0]/2),(core.WINDOW_SIZE[1]/2))

        if core.memory("Vaisseau").NbrVie == 0:
            core.memory("etat", Etat.GAMEOVER)



    if len(core.memory('mesAsteroides')) == 0:
        for i in range(0, 3):
            position_x = random.randint(0, core.WINDOW_SIZE[0])
            position_y = random.randint(-10, 10)
            creationAsteroide(position_x, position_y, 60)




#-------------------Gestion des Vies---------

    if not core.memory("Vie3").ready:
        core.memory("Vie3").load()

    if not core.memory("Vie2").ready:
        core.memory("Vie2").load()

    if not core.memory("Vie1").ready:
        core.memory("Vie1").load()


    if core.memory("Vaisseau").NbrVie == 3:
    #if core.memory("VieV") == 3 :
        core.memory("Vie3").show()
        core.memory("Vie2").show()
        core.memory("Vie1").show()

    if core.memory("Vaisseau").NbrVie == 2:
    #if core.memory("VieV") == 2 :
        core.memory("Vie2").show()
        core.memory("Vie1").show()

    if core.memory("Vaisseau").NbrVie == 1:
    #if core.memory("VieV") == 1 :
        core.memory("Vie1").show()

    if core.memory("Vaisseau").NbrVie == 0:
        core.memory("Vaisseau").NbrVie = 3
        core.memory("Vie3").show()
        core.memory("Vie2").show()
        core.memory("Vie1").show()



    core.cleanScreen()

    if core.getKeyPressList("1"):
        core.memory("VieV", 1)

    if core.getKeyPressList("2"):
        core.memory("VieV", 2)

    if core.getKeyPressList("3"):
        core.memory("VieV", 3)

    #------SCORE-----
    core.Draw.text((255,255,255),"SCORE:",(15,15),35,'Arial')
    core.Draw.text((255,255,255),str(core.memory("total")),(142,15),35,'Arial')


def afficherGameOver():
    core.Draw.text((255, 255, 255), "GAMEOVER", (365, 280), 30)
    core.Draw.text((255, 255, 255), "SCORE:", (15, 15), 35, 'Arial')
    core.Draw.text((255, 255, 255), str(core.memory("total")), (142, 15), 35, 'Arial')

    if core.getKeyPressList("ESCAPE"):
        core.memory("etat", Etat.DEMARRAGE)


def afficherMenu():
    if core.getKeyPressList("ESCAPE"):
        core.memory("etat", Etat.JEU)

    core.Draw.text((255, 255, 255), "JEU EN PAUSE", (420, core.WINDOW_SIZE[1]/2-200), 80, 'Arial')
    core.Draw.text((255, 255, 255), "SCORE :", (535, core.WINDOW_SIZE[1]/2-100), 50, 'Arial')
    core.Draw.text((255, 255, 255), str(core.memory("total")), (715, core.WINDOW_SIZE[1]/2-100), 50, 'Arial')
    core.Draw.rect((255, 255, 255), ((core.WINDOW_SIZE[0] / 2) - 153, (core.WINDOW_SIZE[1] / 2) - 45, 305, 55), 5)
    core.Draw.text((255, 255, 255), "CONTINUER", ((core.WINDOW_SIZE[0] / 2) - 150, (core.WINDOW_SIZE[1] / 2) - 40), 70,'')  # Arial #((core.WINDOW_SIZE[0] / 2) - 105, (core.WINDOW_SIZE[1] / 2) - 60), 105)

    Pos_SourisPlay = pygame.mouse.get_pos()
    recPlay = Rect((core.WINDOW_SIZE[0] / 2) - 153, (core.WINDOW_SIZE[1] / 2) - 45, 305, 55)

    if recPlay.collidepoint(Pos_SourisPlay):
        core.Draw.text((255, 255, 0), "CONTINUER", ((core.WINDOW_SIZE[0] / 2) - 150, (core.WINDOW_SIZE[1] / 2) - 40), 70,'')  # Arial #((core.WINDOW_SIZE[0] / 2) - 105, (core.WINDOW_SIZE[1] / 2) - 60), 105)

        if core.getMouseLeftClick():
            Pos_SourisPlay = core.getMouseLeftClick()

            if recPlay.collidepoint(Pos_SourisPlay):
                core.memory("etat", Etat.JEU)


    core.cleanScreen()



def afficherCredit():
    if core.getKeyPressList("ESCAPE"):
        core.memory("etat", Etat.DEMARRAGE)


    if not core.memory("Credit").ready:
        core.memory("Credit").load()
    core.memory("Credit").show()
    core.cleanScreen()

    core.Draw.text((255, 255, 255), "Meilleur Score : 7000", ((core.WINDOW_SIZE[0] / 2)-465, (core.WINDOW_SIZE[1] / 2)+110), 30,'Cooper Black')
    core.Draw.text((255, 255, 255), "Meilleur Score : 7000",((core.WINDOW_SIZE[0] / 2) +140, (core.WINDOW_SIZE[1] / 2) + 110), 30, 'Cooper Black')


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
