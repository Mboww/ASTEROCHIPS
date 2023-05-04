from agario.map import Map
from agario.player import Player


class Partie:
    def __init__(self):
        self.map = Map()
        self.player = Player()

    def controle(self):
        self.player.deplacement()

    def addPlayer(self):
        p = Player()
        p.bot = False # pour dire que c'est pas un bot
        self.map.addJoueur(p)  # dans la classe map on appelle la fonction addJoueur sur 'p' un player particulier

    def addBots(self):
        for i in range(0, self.map.maxPlayer):
            self.map.addJoueur(Player())  # crée un joueur par défaut

    def show(self):
        self.map.show()  # utilise la méthode show dans la classe map
