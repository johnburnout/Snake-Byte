# -*- coding:Utf8 -*-

# ##################
# Snake Byte v1.0  #
#   Jean Roussie   #
# jean@roussie.net #
# ##################


import tkinter.font as tkfont
from random import randint
from serpent import Serpent
from pomme import Pomme
from preferences import *
from apropos import *


class BarreMenu(Frame):
    """Barre de menus"""
    def __init__(self, boss):
        Frame.__init__(self, boss)
        self.configure(bg="light grey")
        menu_fichier = Menubutton(self, text="SnakeByte", bg="light grey", relief=RAISED, border=5,
                                  font=('Helvetica', 14), width=12)
        menu_fichier.pack(side=LEFT, padx=5, pady=5)
        self.menuFichier = Menu(menu_fichier)
        self.menuFichier.add_command(label="A propos", command=boss.a_propos, font=('Helvetica', 14))
        self.menuFichier.add_separator()
        self.menuFichier.add_command(label="Préférences", command=boss.preferences, font=('Helvetica', 14))
        self.menuFichier.add_command(label="Quitter", command=quit, font=('Helvetica', 14))
        
        menu_fichier.configure(menu=self.menuFichier)


class SnakeByte(Tk):    # la classe SnakeByte dérive de la classe Tk de tkinter et hérite de toutes ses méthodes
    def __init__(self):
        """Construction de la fenêtre principale"""

        Tk.__init__(self)
        self.title('Snake Byte')
        self.geometry("+100+100")
        self.configure(bg='light grey')
        self.resizable(width=False, height=False)    # Fenètre non redimensionnable manuellement
        [self.largeur, self.son] = init_largeur()
        self.hauteur = 3*self.largeur//4
        self.croque = 0
        self.fini = 1
        
        # --- Polices de caractères

        self.helv18 = tkfont.Font(family='Helvetica', size=18)
        self.helv18b = tkfont.Font(family='Helvetica', size=18, weight='bold')
        self.helv24 = tkfont.Font(family='Helvetica', size=24)
        self.helv24b = tkfont.Font(family='Helvetica', size=24, weight='bold')
        self.helv36 = tkfont.Font(family='Helvetica', size=36, weight='bold')
        
        # --- Intialisation des variables Tkinter

        self.score = StringVar()
        self.hiScore = StringVar()
        self.largstr = StringVar()
        self.largstr.set(str(self.largeur))

        self.hiScore.set(self.lecture_hi_score(self.largeur))
        self.terrain = Canvas(self)
        self.terrain.configure(width=self.largeur*20, height=self.hauteur*20, bg="green")
        self.terrain.grid(row=10, columnspan=5, padx=5, pady=5)
        
        self.menu = BarreMenu(self)
        self.menu.grid(row=0, columnspan=4, column=0, sticky=W)
        
        Label(self, text='Snake Byte', font=self.helv36, bg='green',
              fg="#cc9f26").grid(row=9, column=2, padx=25, pady=5)

        Label(self, text='Score :', font=self.helv18).grid(row=9, column=0, padx=5, pady=5, sticky=E)
        Label(self, textvariable=self.score,
              font=self.helv18b, bg='light grey').grid(row=9, column=1, padx=5, pady=5, sticky=W)
        Label(self, text='Hi Score :', font=self.helv18).grid(row=9, column=3, padx=5, pady=5, sticky=E)
        Label(self, textvariable=self.hiScore,
              font=self.helv18b, bg='dark grey', fg='white').grid(row=9, column=4, padx=5, pady=5, sticky=W)
        Label(self, text='Largeur :',
              font=self.helv18, bg='light grey').grid(row=11, column=0, padx=5, pady=5, sticky=E)
        Label(self, textvariable=self.largstr,
              font=self.helv18b, bg='light grey', fg='black') \
            .grid(row=11, column=1, padx=5, pady=5, sticky=W)
        Label(self, text='Démarrer : [Espace] - Diriger le serpent : [<-] [->]', bg='dark grey', fg='white')\
            .grid(row=11, column=2, columnspan=3, pady=5)
        
        self.serpent = Serpent(self.terrain, self.largeur, self.hauteur)
        self.pomme = Pomme(self.terrain)
        
        self.bind("<Left>", self.serpent.tourne_gauche)
        self.bind("<Right>", self.serpent.tourne_droite)
        self.bind("<space>", self.depart)
        self.bind("<Escape>", self.quitter)
        self.scores = {}

        self.gameOver = None
        self.prefs = None
        self.aPropos = None

        self.mainloop()

    def deplace_pomme(self):
        """Déplace la pomme"""

        x, y = 0, 0
        test = 0
        while test == 0:
            test = 1
            x = randint(1, self.largeur)
            y = randint(1, self.hauteur)
            for piece in self.serpent.corps:
                if x == piece[0] and y == piece[1]:
                    test = 0
        self.pomme.deplace_pomme(x, y)

    def depart(self, event):
        """Initialisation et lancement du jeu"""
        
        if self.fini:
            
            # Réinitialisation des paramètres du jeu
                    
            self.score.set('0')
            # self.terrain.delete(self.gameOver)
            try:
                self.terrain.delete(self.gameOver)
            except AttributeError:
                pass
            self.fini = 0
            
            [self.largeur, self.son] = init_largeur()
            self.hauteur = 3*self.largeur//4
            self.terrain.configure(width=self.largeur*20, height=self.hauteur*20, bg="green")

            self.largstr.set(str(self.largeur))
            
            self.hiScore.set(self.lecture_hi_score(self.largeur))
            
            # self.serpent.initialisation()
            
            self.serpent.__init__(self.terrain, self.largeur, self.hauteur)
            self.quitter_prefs()

            self.deplace_pomme()
            self.deplacement()   # Lancement de l'animation
            
    def fin(self):
        """Terminer le jeu"""

        if self.son == 'On':
            self.bell()
        self.gameOver = self.terrain.create_text(20*self.largeur//2, 20*self.hauteur//2,
                                                 text='Game Over', font=self.helv36, fill='white')
        fichier = open('usager/hiscore', 'w')  # ouverture d'un fichier vierge d'écriture des high scores
        fichier.write(str(self.scores))
        fichier.close()
        self.ecriture_hi_score(self.largeur)
    
    def quitter(self, event):
        """Quitter le jeu"""

        self.quit()

    def deplacement(self):
        """Modification du serpent"""

        if not self.fini:
            self.fini = self.serpent.deplacement(self.croque)
            if (self.serpent.corps[0][0], self.serpent.corps[0][1]) == (self.pomme.x, self.pomme.y):
                if self.son == 'On':
                    self.bell()
                self.croque = 1
                self.score.set(str(eval(self.score.get()+"+1")))
                if eval(self.score.get()) > eval(self.hiScore.get()):
                    self.hiScore.set(self.score.get())
                self.deplace_pomme()
            else:
                self.croque = 0
            self.after(75, self.deplacement) 
        else:
            self.fin()
            
    def lecture_hi_score(self, largeur):
        
        self.scores = {}
        try:
            fichier = open('usager/hiscore', 'r')  # ouverture du fichier de stockage des high score en lecture
            self.scores = eval(fichier.read())
            fichier.close()
            hiscore = str(self.scores[largeur])
        except FileNotFoundError:
            hiscore = "0"
        return hiscore
    
    def ecriture_hi_score(self, largeur):
        
        self.scores[largeur] = int(self.hiScore.get())
        fichier = open('usager/hiscore', 'w')
        fichier.write(str(self.scores))
        fichier.close()
        
    def preferences(self, event=None):

        self.menu.menuFichier.entryconfigure(2, state=DISABLED)
        self.prefs = Preferences(self)
        
    def quitter_prefs(self, event=None):
        self.menu.menuFichier.entryconfigure(2, state=NORMAL)
        try:
            self.prefs.destroy()
        except AttributeError:
            pass
            
    def a_propos(self, event=None):

        self.menu.menuFichier.entryconfigure(0, state=DISABLED)
        self.aPropos = APropos(self)
        
    def quitter_a_propos(self, event=None):
        self.menu.menuFichier.entryconfigure(0, state=NORMAL)
        try:
            self.aPropos.destroy()
        except AttributeError:
            pass
            
# Programme principal


if __name__ == "__main__":

    f = SnakeByte()
