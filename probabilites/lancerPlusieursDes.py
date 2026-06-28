# Modifier cette ligne pour duplique le programme avant de le lancer

from jetdedes import *
import matplotlib.pyplot as plt

nbDes, nbFaces, nbTirages, tirages = 0, 0, 0, 0  # Initialisation des variables

# Saisie des variables :

while nbDes < 1 or nbDes > 10:
    saisie = input('Entrer le nombre de dés (nbDes≤10, par défaut 2): ')
    if saisie:
        nbDes = int(saisie)
    else:
        nbDes = 2

while nbFaces < 1 or nbFaces > 20:
    saisie = input('Entrer le nombre de faces (nbFaces≤20, par défaut 6): ')
    if saisie:
        nbFaces = int(saisie)
    else:
        nbFaces = 6

while nbTirages < 1 or nbTirages > 1000000:
    saisie = input('Entrer le nombre de tirages (nbTirages≤1 000 000, par défaut 10): ')
    if saisie:
        nbTirages = int(saisie)
    else:
        nbTirages = 10

resultats = []  # Résultats des tirages
for i in range(nbDes, nbDes * nbFaces + 1):
    resultats.append(0)

# Tirages
print("\n--------\nTirages\n--------\n")

for i in range(nbTirages):  # nouvelle séquence
    res = 0
    for k in range(nbDes):
        res = res + lancerUnDe(nbFaces)  # lancer de dé
    resultats[res - nbDes] += 1  # mémorisation du résultat
    tirages += 1

print("\n--------\nSynthese\n--------\n")
frequences = []
for i in range(nbDes * nbFaces - nbDes + 1):
    frequences.append(resultats[i] / tirages)
    print("Le {:d} est sorti {:d} fois, sa fréquence est {:1.4f}".format(
        (i + nbDes), resultats[i], frequences[i]))

# Data for plotting
issues = range(nbDes, nbDes * nbFaces + 1)
plt.bar(issues, frequences)
plt.xlabel(" Issues")
plt.ylabel(" Fréquences")
plt.title(str(nbTirages) + " tirages de " + str(nbDes) + " dés à " + str(nbFaces) + " faces")
# plt.xlim(1, 6)
plt.ylim(0, max(frequences) * 1.2)

plt.show()
