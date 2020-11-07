# -*- coding:Utf8 -*-

####################
# Snake Byte v0.b2 #
#   Jean Roussie   #
# jean@roussie.net #
####################    

from tkinter import *
import tkinter.font as tkFont
from random import randint
from serpent import Serpent
from pomme import Pomme
from preferences import *



class SnakeByte(Tk) :    #la classe SnakeByte dérive de la classe Tk de tkinter et hérite de toutes ses méthodes
    def __init__(self):
        """Construction de la fenêtre principale"""
        Tk.__init__(self)
        self.title('Snake Byte')
        self.geometry("+100+100")
        self.configure(bg='light grey')
        self.resizable(width =0, height =0) # Fenètre non redimensionnable manuellement
        [self.largeur, self.son] = initLargeur()
        self.hauteur = 3*self.largeur//4
        self.croque = 0
        self.fini = 1
        
        #--- Polices de caractères

        self.helv18 = tkFont.Font(family='Helvetica', size=18)
        self.helv18b = tkFont.Font(family='Helvetica', size=18, weight='bold')
        self.helv24 = tkFont.Font(family='Helvetica', size=24)
        self.helv24b = tkFont.Font(family='Helvetica', size=24, weight='bold')
        self.helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
        
        #--- Intialisation des variables Tkinter

        self.score = StringVar()
        self.hiScore = StringVar()
        self.largstr = StringVar()
        self.largstr.set(str(self.largeur))

        self.hiScore.set(self.lectureHiScore(self.largeur))
        self.terrain = Canvas(self)
        self.terrain.configure(width=self.largeur*20, height=self.hauteur*20, bg="green")
        self.terrain.grid(row=10, columnspan=5, padx=5, pady=5)
        
        Label(self, text='Snake Byte', font=self.helv36, bg='green', fg="#cc9f26").grid(row=9, column=2, padx=25, pady=5)

        Label(self, text = 'Score :', font=self.helv18).grid(row=9, column=0, padx=5, pady=5, sticky=E)
        Label(self, textvariable = self.score, font=self.helv18b, bg='light grey').grid(row=9, column=1, padx=5, pady=5, sticky=W)
        Label(self, text = 'Hi Score :', font=self.helv18).grid(row=9, column=3, padx=5, pady=5, sticky=E)
        Label(self, textvariable = self.hiScore, font=self.helv18b, bg='dark grey', fg='white').grid(row=9, column=4, padx=5, pady=5, sticky=W)
        Label(self, text = 'Largeur :', font=self.helv18, bg='light grey').grid(row=11, column=0, padx=5, pady=5, sticky=E)
        self.afficheLargeur = Label(self, textvariable = self.largstr, font=self.helv18b, bg='light grey', fg='black').grid(row=11, column=1, padx=5, pady=5, sticky=W)
        Label(self, text='Démarrer : [Espace] - Diriger le serpent : [<-] [->]\nPréférences :[P] - Quitter : [esc]', bg='dark grey', fg='white').grid(row=11, column= 2, columnspan=3, pady=5)
        
        self.serpent = Serpent(self.terrain, self.largeur, self.hauteur)
        self.pomme = Pomme(self.terrain)
        
        self.bind("<Left>", self.serpent.tourneGauche)
        self.bind("<Right>", self.serpent.tourneDroite)
        self.bind("<space>", self.depart)
        self.bind("<Escape>", self.quitter)
        self.bind("<p>", self.preferences)        
        self.bind("<P>", self.preferences)
        
        self.mainloop()
    def depart(self, event) :
        "Initialisation et lancement du jeu"
        
        if self.fini :
            
            # Réinitialisation des paramètres du jeu
                    
            self.score.set('0')
            try :
                self.terrain.delete(self.gameOver)
            except :
                None
            self.fini = 0
            
            [self.largeur, self.son] = initLargeur()
            self.hauteur = 3*self.largeur//4
            self.terrain.configure(width=self.largeur*20, height=self.hauteur*20, bg="green")

            
            self.largstr.set(str(self.largeur))
            
            self.hiScore.set(self.lectureHiScore(self.largeur))
            
            #self.serpent.initialisation()
            
            self.serpent.__init__(self.terrain, self.largeur, self.hauteur)
            try :
                self.quitterPrefs()
            except :
                None
            test = 0
            while test == 0 :
                test = 1
                x =randint(1, self.largeur)
                y =randint(1, self.hauteur)
                #print(str(x)+" "+str(y))
                for piece in self.serpent.corps :
                    if x == piece[0] and y == piece[1] :
                        test = 0
            self.pomme.deplacePomme(x, y)
            self.deplacement() # Lancement de l'animation
            
    def fin(self) :        
        "Terminer le jeu"
        if self.son == 'On' :
            self.bell()
        self.gameOver = self.terrain.create_text(20*self.largeur//2, 20*self.hauteur//2, text='Game Over', font=self.helv36, fill='white')
        fichier = open('hiscore', 'w') # ouverture d'un fichier vierge d'écriture des high scores
        fichier.write(str(self.scores))
        fichier.close()
        self.ecritureHiScore(self.largeur)
    
    def quitter(self, event) :
        "Quitter le jeu"
        self.quit()

    def deplacement(self) :
        "Modification du serpent"
        if not self.fini :
            self.fini = self.serpent.deplacement(self.croque)
            if (self.serpent.corps[0][0], self.serpent.corps[0][1]) == (self.pomme.x, self.pomme.y) :
                if self.son == 'On' :
                    self.bell()
                self.croque = 1
                self.score.set(str(eval(self.score.get()+"+1")))
                if eval(self.score.get()) > eval(self.hiScore.get()) :           
                    self.hiScore.set(self.score.get())
                test = 0
                while test == 0 :
                    test = 1
                    x =randint(1, self.largeur)
                    y =randint(1, self.hauteur)
                    #print(str(x)+" "+str(y))
                    for piece in self.serpent.corps :
                        if x == piece[0] and y == piece[1] :
                            test = 0
                self.pomme.deplacePomme(x, y)
            else :
                self.croque = 0
            self.after(75, self.deplacement) 
        else :
            self.fin()
            
    def lectureHiScore(self, largeur) :
        
        self.scores = {}
        try :
            fichier = open('hiscore', 'r') # ouverture du fichier de stockage des high score en lecture
            self.scores = eval(fichier.read())
            fichier.close()
            hiscore = str(self.scores[largeur])
        except :
           hiscore = "0"
        return hiscore
    
    def ecritureHiScore(self, largeur) :
        
        self.scores[largeur] = int(self.hiScore.get())
        fichier = open('hiscore', 'w')
        fichier.write(str(self.scores))
        fichier.close()
        
    def preferences(self, event) :
        try :
            self.prefs.destroy()
        except :
            None
        self.prefs = Preferences(self)
        
    def quitterPrefs(self) :
        self.prefs.destroy()
            
# Programme principal

if __name__ == "__main__" :

    SnakeByte()