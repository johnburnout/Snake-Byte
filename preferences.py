# -*- coding:Utf8 -*-

# ##################
# Snake Byte v1.0  #
#   Jean Roussie   #
# jean@roussie.net #
# ##################

import tkinter
from chemins import fichier_usager


def init_largeur():
    try:
        f = open(fichier_usager("prefs"), "r")
        larg = int(f.readline())
        son = f.readline()
        f.close()
    except FileNotFoundError:
        larg = 40
        son = 'On'
    return [larg, son]


class Preferences(tkinter.Toplevel):
    """Classe de fenêtre de préférences"""
    
    def __init__(self, boss=None, **arguments):
        tkinter.Toplevel.__init__(self, **arguments)
        self.boss = boss
        self.title('Préférences du Snake Byte')
        self.geometry("340x130+200+150")
        self.configure(bg="light grey")
        self.resizable(width=False, height=False)
        self.overrideredirect(True)
        self.transient(self.boss)
        [largeur, son] = init_largeur()
        self.curseur = tkinter.Scale(self, length=300, orient=tkinter.HORIZONTAL,
                                     label="Largeur du terrain :", bg="light grey",
                                     troughcolor="dark grey", showvalue=True, from_=20, to=60,
                                     tickinterval=20, resolution=4)
        self.curseur.set(largeur)
        self.son = tkinter.StringVar()
        self.son.set(son)
        self.curseur.grid(row=0, padx=20, pady=5, column=0, columnspan=2)
        
        self.choixSon = tkinter.Frame(self, bg='light grey')
        self.choixSon.grid(padx=5, pady=5, row=1, column=0)
        vals = ['On', 'Off']
        tkinter.Label(self.choixSon, text="Son : ", bg='light grey').pack(side=tkinter.LEFT)
        for i in range(2):
            tkinter.Radiobutton(self.choixSon, variable=self.son, text=vals[i],
                                value=vals[i], bg='light grey').pack(side=tkinter.LEFT)

        tkinter.Button(self, text="Enregistrer", command=self.valider, bg="light grey",
                       activebackground="dark grey", borderwidth=1).grid(padx=5, pady=5, row=1, column=1)
        
        self.mainloop()
        
    def valider(self):
        f = open(fichier_usager("prefs"), "w")
        f.write("{}\n{}".format(self.curseur.get(), self.son.get()))
        f.close()
        self.boss.son = self.son.get()
        print('grrrr')
        self.boss.quitter_prefs()
        self.destroy()
    

if __name__ == "__main__":
    prefs = Preferences()
