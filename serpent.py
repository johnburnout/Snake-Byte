# -*- coding:Utf8 -*-

# ###################
# Snake Byte v1.0   #
# Jean Roussie      #
# jean@roussie.net  #
# ###################

from tkinter import PhotoImage


class Serpent(object):
    """Classe de corps"""
    
    def __init__(self, canevas, largeur, hauteur):
        """Initialisation du corps"""
        
        self.canevas, self.largeur, self.hauteur = canevas, largeur, hauteur
        
        # --- Intialisation des variables
        
        self.img_tete = [PhotoImage(file="images/tete_E.png"), PhotoImage(file="images/tete_S.png"),
                         PhotoImage(file="images/tete_W.png"), PhotoImage(file="images/tete_N.png")]
        self.img_queue = [PhotoImage(file="images/queue_E.png"), PhotoImage(file="images/queue_S.png"),
                          PhotoImage(file="images/queue_W.png"), PhotoImage(file="images/queue_N.png")]
        self.img_corps = PhotoImage(file="images/corps.png")

        # Mise en place du serpent en position de départ
        self.orientationTete = 0
        self.dx = 1
        self.dy = 0
        self.croque = 0

        self.corps = [
            [1, self.hauteur // 2, 0,
             self.canevas.create_image(20 * 1 - 10, self.hauteur // 2 * 20 - 10, image=self.img_tete[0])],
            [0, self.hauteur // 2, 0,
             self.canevas.create_image(19 * 0 - 10, self.hauteur // 2 * 20 - 10, image=self.img_queue[0])]
        ]

    def tourne_gauche(self, event):
        """tourner à gauche"""
        
        if self.orientationTete == 0:
            self.dx = 0
            self.dy = -1
            self.orientationTete = 3
        elif self.orientationTete == 1:
            self.dx = 1
            self.dy = 0
            self.orientationTete = 0
        elif self.orientationTete == 2:
            self.dx = 0
            self.dy = 1
            self.orientationTete = 1
        else:
            self.dx = -1
            self.dy = 0
            self.orientationTete = 2

    def tourne_droite(self, event):
        """tourner à droite"""
        
        if self.orientationTete == 0:
            self.dx = 0
            self.dy = 1
            self.orientationTete = 1
        elif self.orientationTete == 1:
            self.dx = -1
            self.dy = 0
            self.orientationTete = 2
        elif self.orientationTete == 2:
            self.dx = 0
            self.dy = -1
            self.orientationTete = 3
        else:
            self.dx = 1
            self.dy = 0
            self.orientationTete = 0

    def deplacement(self, croque):
        """déplacement du serpent d'une case"""

        self.croque = croque
        longueur = len(self.corps)
        x, y = self.corps[0][0]+self.dx, self.corps[0][1]+self.dy
        self.canevas.delete(self.corps[longueur-1][3])
        if self.croque == 0:
            del self.corps[longueur - 1]
            longueur = longueur - 1
        longueur = longueur + 1
        self.corps.insert(0,
                          [x, y, self.orientationTete,
                           self.canevas.create_image(20*x-10, 20*y-10, image=self.img_tete[self.orientationTete])])
        self.canevas.itemconfigure(self.corps[1][3], image=self.img_corps)
        self.canevas.itemconfigure(self.corps[longueur-1][3], image=self.img_queue[self.corps[longueur-2][2]])
        fini = 0
        if x > self.largeur or x <= 0 or y > self.hauteur or y <= 0:    # Le corps touche-t-il le bord ?
            fini = 1
        for piece in self.corps[3:-1]:    # Le corps se mord-il la queue ?
            if x == piece[0] and y == piece[1]:
                fini = 1
        return fini
