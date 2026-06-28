import random

def lancerUnDe(n=6):
  """
Petit programme simple simulant le lancer d'un dé
dont le nombre de faces est entré comme paramètre.
Par défaut le nombre de faces est 6
"""

  d = random.randint(1, n)
  return d