from tkinter import *
import tkinter.font as tkFont
from random import randint
from serpent import *
from pomme import *

class SnakeByte(object) :
    def __init__(self):
        """Construction de la fenêtre principale"""
        self.root = Tk()
        self.root.title('Snake Byte')
        self.root.configure(bg='light grey')
        
        self.largeur, self.hauteur = 30, 25
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

        self.score.set("0")

        try :
            fichier = open('hiscore', 'r') # ouverture du fichier de stockage des high score en lecture
            self.hiScore.set(fichier.read())
            fichier.close()
        except :
            self.hiScore.set("0")
        
        self.terrain = Canvas(self.root, width=self.largeur*20, height=self.hauteur*20, bg="green")
        self.terrain.grid(row=1, columnspan=5, padx=5, pady=5)

        Label(self.root, text = 'Score :', font=self.helv18).grid(row=0, column=0, padx=5, pady=5, sticky=E)
        Label(self.root, textvariable = self.score, font=self.helv18b, bg='light grey').grid(row=0, column=1, padx=5, pady=5, sticky=W)
        Label(self.root, text = 'Hi Score :', font=self.helv18).grid(row=0, column=3, padx=5, pady=5, sticky=E)
        Label(self.root, textvariable = self.hiScore, font=self.helv18b, bg='dark grey', fg='white').grid(row=0, column=4, padx=5, pady=5, sticky=W)

        Label(self.root, text='Snake Byte', font=self.helv36, bg='green', fg="#cc9f26").grid(row=0, column=2, padx=25, pady=5)
        Label(self.root, text='Démarrer : [Espace] - Diriger le serpent : [<-] [->] - Quiter : [esc]', bg='light grey', fg='black').grid(row=2, columnspan=5, pady=5)

        self.gameOver = self.terrain.create_text(20*self.largeur//2, 20*self.hauteur//2, text='', font=self.helv36, fill='white')
        
        self.serpent = Serpent(self.terrain, self.largeur, self.hauteur)
        self.pomme = Pomme(self.terrain)
        
        self.root.bind_all("<Left>", self.serpent.tourneGauche)
        self.root.bind_all("<Right>", self.serpent.tourneDroite)
        self.root.bind_all("<space>", self.depart)
        self.root.bind_all("<Escape>", self.quitter)
        
        self.root.mainloop()
        
    def depart(self, event) :
        "Initialisation et lancement du jeu"
        
        if self.fini :
            
            # Réinitialisation des paramètres du jeu
                    
            self.score.set('0')
            self.terrain.delete(self.gameOver)
            self.fini = 0
            self.terrain.delete(self.gameOver)
            
            self.serpent.initialisation()
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

        self.terrain.delete(self.gameOver)
        self.gameOver = self.terrain.create_text(20*self.largeur//2, 20*self.hauteur//2, text='Game Over', font=self.helv36, fill='white')
        
        fichier = open('hiscore', 'w') # ouverture d'un fichier vierge d'écriture des high scores
        fichier.write(self.hiScore.get())
        fichier.close()
    
    def quitter(self, event) :
        "Quitter le jeu"
        
        self.root.quit()

    def deplacement(self) :
        "Modification du serpent"
        if not self.fini :
            self.fini = self.serpent.deplacement(self.croque)
            if (self.serpent.corps[0][0], self.serpent.corps[0][1]) == (self.pomme.x, self.pomme.y) :
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
            self.root.after(75, self.deplacement) 
        else :
            self.fin()

# Programme principal

if __name__ == "__main__" :
    jeu = SnakeByte()