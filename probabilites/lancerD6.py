# Modifier cette ligne pour duplique le programme avant de le lancer

from jetdedes import *
import matplotlib.pyplot as plt

nbTirages, tirages, resultats = 0, 0, [0, 0, 0, 0, 0,
                                       0]  # Initialisation variables

# Saisie du nombre de tirages par séquence et du nombre de séquences

while nbTirages < 1 or nbTirages > 1000000:
    saisie = input(
        'Entrer le nombre de tirages (n≤1 000 000, par défaut 10): ')
    if saisie:
        nbTirages = int(saisie)
    else:
        nbTirages = 10

print("\n--------\nTirages\n--------\n")

# Tirages

for i in range(nbTirages):  # nouvelle séquence
    issue = lancerUnDe()  # lancer de dé
    resultats[issue - 1] += 1  # mémorisation du résultat
    tirages += 1

print("\n--------\nSynthese\n--------\n")
frequences = []
for i in range(6):
    frequences.append(resultats[i] / tirages)
    print("Le {:d} est sorti {:d} fois, sa fréquence est {:1.4f}".format(
        (i + 1), resultats[i], frequences[i]))

# Data for plotting
issues = [1, 2, 3, 4, 5, 6]
plt.bar(issues, frequences)
plt.xlabel(" Issues : faces du dé")
plt.ylabel(" Fréquences")
plt.title(str(nbTirages) + " tirages d'un dé à 6 faces")
# plt.xlim(1, 6)
plt.ylim(0, max(frequences) * 1.2)

plt.show()
