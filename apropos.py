# -*- coding:Utf8 -*-

# Snake Byte v1.0 #
#   Jean Roussie   #
# jean@roussie.net #

from tkinter import *


class APropos(Toplevel):
    """Classe de fenêtre d'information"""

    def __init__(self, boss=None, **arguments):
        Toplevel.__init__(self, **arguments)
        self.boss = boss
        self.title('A propos de Snake Byte')
        self.geometry("+150+120")
        self.configure(bg="light grey")
        self.resizable(width=False, height=False)
        self.overrideredirect(True)
        self.transient(self.boss)
        Label(self, text="Snake Byte, un jeu en Python\n",
              bg='light grey', justify='center').grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        Label(self, text="--------------------------------\nInspiré librement d'un vieux jeu\n" +
                         "qui tournait sur Apple ][\n" +
                         "--------------------------------",
              bg='light grey', justify='center').grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        Label(self, text="\nAppuyer sur \'Espace\' pour lancer le jeu\n" +
                         "Sur \'<-\' et \'->\' pour diriger le serpent\n\n" +
                         "--------------------------------\n" +
                         "Jean Roussie - maths.roussie.net",
              bg='light grey', justify='center').grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        Button(self, text="Fermer", command=self.quitter, bg='light grey',
               relief=RAISED).grid(row=10, column=2, padx=5, pady=5)
        
        self.mainloop()
        
    def quitter(self):
        self.boss.quitter_a_propos()
        self.destroy()


if __name__ == "__main__":
    prefs = APropos()
