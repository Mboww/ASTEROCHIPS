import core
from agario.partie import Partie
from agario.player import Player


def setup(): #exécution une seule fois au démarrage
    print("start setup")
    core.WINDOW_SIZE = [1200,700]
    core.fps = 60

    core.memory(("partie"), Partie()) #création dans mémoire : nom de la variable et classe associé
    core.memory("partie").addPlayer()
    core.memory("partie").addBots() #dans la varible partie j'appelle la fonction addBot
    core.memory(("player"), Player())
    core.memory("player").deplacement()
    print("End setup")

def run(): #exécution à chaque frame

    core.cleanScreen() #aucune mémoire à chaque frame (rappel: 60frame/seconde)

    core.memory("partie").show()
    #1, récupère la variable qui s'appelle partie et le 2e récupère la méthode show dans la classe partie
    print("end run")

core.main(setup, run)
