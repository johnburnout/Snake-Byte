# -*- coding:Utf8 -*-

####################
# Snake Byte v0.b2 #
#   Jean Roussie   #
# jean@roussie.net #
####################    

from tkinter import *

def initLargeur() :
    try :
        f = open("prefs", "r")
        larg = int(f.readline())
        son = f.readline()
        f.close()
    except :
        larg = 40
        son = 'On'
    return [larg,son]

class Preferences(Toplevel) :
    "Classe de fenêtre de préférences"
    
    def __init__(self, boss, **Arguments):
        Toplevel.__init__(self, boss, **Arguments)
        self.boss = boss
        self.title('Préférences du Snake Byte')
        self.geometry("340x130+200+150")
        self.configure(bg="light grey")
        self.resizable(width =0, height =0) 
        [largeur, son] = initLargeur()
        self.curseur = Scale(self, length=300, orient=HORIZONTAL, label="Largeur du terrain :", bg="light grey",
            troughcolor="dark grey", showvalue = 40, from_=20, to=60, tickinterval=20, resolution = 4)
        self.curseur.set(largeur)
        self.son = StringVar()
        self.son.set(son)
        self.curseur.grid(row=0, padx=20, pady=5, column=0, columnspan=2)
        
        self.choixSon = Frame(self, bg='light grey')
        self.choixSon.grid(padx=5, pady=5, row=1, column=0)
        vals =['On','Off']
        Label(self.choixSon, text="Son : ", bg='light grey').pack(side=LEFT)
        for i in range(2) :
            Radiobutton(self.choixSon, variable=self.son, text=vals[i], value=vals[i], bg='light grey').pack(side=LEFT)
            
            
        
        Button(self ,text="Enregistrer", command=self.valider, bg="light grey",
            activebackground="dark grey", borderwidth=1).\
            grid(padx=5, pady=5, row=1, column=1)
        
        #self.bind_all("<escape>", valider)
        self.mainloop()
        
    def valider(self) :
        f = open("prefs", "w")
        f.write("{}\n{}".format(self.curseur.get(),self.son.get()))
        f.close()
        self.boss.son = self.son.get()
        self.destroy()
    
if __name__ == "__main__" :
    prefs = Preferences()