# Modifier cette ligne pour duplique le programme avant de le lancer
import random
import matplotlib.pyplot as plt


def Tirage(p=0.5):
    ## Tirage aléatoir d'un évènement de probabilité p
    if random.random() <= p:
        return True
    else:
        return False


# initialisation des variables :

issuesFavorables, probabilite, nbTirages, frequences, tirages = 0, -1, 0, [], []

# paramètres du graphique :

precisionPlot = 500  # limite du traçage systématique
intervallePoints = nbTirages // precisionPlot + 1  # nombre de tirages entre deux points au dessus de la limite

# saisie des paramètres

while probabilite < 0 or probabilite > 1:
    saisie = input('Probabilité de réussite de l\'expérience (0≤p≤1, par défaut 0.5): ')
    if saisie:
        probabilite = float(saisie)
    else:
        probabilite = 0.5

while nbTirages < 1 or nbTirages > 1000000:
    saisie = input('Nombre de tirages  (n≤1 000 000, par défaut 20): ')
    if saisie:
        nbTirages = int(saisie)
    else:
        nbTirages = 20

# Tirages

print("\n--------\nTirages\n--------\n")

for i in range(nbTirages):
    if Tirage(probabilite):
        issuesFavorables += 1
    if i <= precisionPlot or not i % intervallePoints:
        tirages.append(i + 1)
        frequences.append(issuesFavorables / (i + 1))

# Graphique

print("\n--------\nGraphique\n--------\n")

plt.scatter(tirages, frequences, marker=".")
plt.plot([0, nbTirages + 0.05], [probabilite, probabilite], color="red")
plt.xlabel(" Tirages")
plt.ylabel(" Fréquences")
plt.title(str(nbTirages) + " tirages avec probabilité de réussite de " + str(probabilite))

plt.ylim(-0.01, 1.01)
plt.xlim(0.95, nbTirages + 0.05)

plt.show()