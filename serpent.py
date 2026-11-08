# -*- coding:Utf8 -*-

# ###################
# Snake Byte v1.0   #
# Jean Roussie      #
# jean@roussie.net  #
# ###################

from tkinter import PhotoImage
from chemins import ressource

# Déplacement (dx, dy) pour chaque orientation : Est, Sud, Ouest, Nord
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
VIRAGES_MAX = 3    # nombre de virages gardés en mémoire d'avance


class Serpent(object):
    """Classe de corps"""
    
    def __init__(self, canevas, largeur, hauteur):
        """Initialisation du corps"""
        
        self.canevas, self.largeur, self.hauteur = canevas, largeur, hauteur
        
        # --- Intialisation des variables
        
        self.img_tete = [PhotoImage(file=ressource("images/tete_E.png")), PhotoImage(file=ressource("images/tete_S.png")),
                         PhotoImage(file=ressource("images/tete_W.png")), PhotoImage(file=ressource("images/tete_N.png"))]
        self.img_queue = [PhotoImage(file=ressource("images/queue_E.png")), PhotoImage(file=ressource("images/queue_S.png")),
                          PhotoImage(file=ressource("images/queue_W.png")), PhotoImage(file=ressource("images/queue_N.png"))]
        self.img_corps = PhotoImage(file=ressource("images/corps.png"))

        # Mise en place du serpent en position de départ
        self.orientationTete = 0    # 0 : Est, 1 : Sud, 2 : Ouest, 3 : Nord
        self.dx, self.dy = DIRECTIONS[0]
        self.croque = 0
        self.virages = []    # virages demandés, appliqués un par case parcourue

        self.corps = [
            [1, self.hauteur // 2, 0,
             self.canevas.create_image(20 * 1 - 10, self.hauteur // 2 * 20 - 10, image=self.img_tete[0])],
            [0, self.hauteur // 2, 0,
             self.canevas.create_image(20 * 0 - 10, self.hauteur // 2 * 20 - 10, image=self.img_queue[0])]
        ]

    def efface(self):
        """Efface le serpent du canevas"""

        for piece in self.corps:
            self.canevas.delete(piece[3])

    def tourne_gauche(self, event):
        """tourner à gauche"""

        if len(self.virages) < VIRAGES_MAX:
            self.virages.append(-1)

    def tourne_droite(self, event):
        """tourner à droite"""

        if len(self.virages) < VIRAGES_MAX:
            self.virages.append(1)

    def deplacement(self, croque):
        """déplacement du serpent d'une case"""

        # Un seul virage par case : deux appuis rapides ne peuvent plus faire
        # faire demi-tour au serpent sur place (il se traversait lui-même)
        if self.virages:
            self.orientationTete = (self.orientationTete + self.virages.pop(0)) % 4
            self.dx, self.dy = DIRECTIONS[self.orientationTete]

        self.croque = croque
        x, y = self.corps[0][0]+self.dx, self.corps[0][1]+self.dy
        if self.croque == 0:    # La queue avance, sauf si le serpent grandit
            self.canevas.delete(self.corps[-1][3])
            del self.corps[-1]
        self.corps.insert(0,
                          [x, y, self.orientationTete,
                           self.canevas.create_image(20*x-10, 20*y-10, image=self.img_tete[self.orientationTete])])
        self.canevas.itemconfigure(self.corps[1][3], image=self.img_corps)
        self.canevas.itemconfigure(self.corps[-1][3], image=self.img_queue[self.corps[-2][2]])
        fini = 0
        if x > self.largeur or x <= 0 or y > self.hauteur or y <= 0:    # Le corps touche-t-il le bord ?
            fini = 1
        for piece in self.corps[1:]:    # Le corps se mord-il la queue ?
            if x == piece[0] and y == piece[1]:
                fini = 1
        return fini
