# -*- coding:Utf8 -*-

# ##################
# Snake Byte v1.0  #
#   Jean Roussie   #
# jean@roussie.net #
# ##################

"""Chemins des ressources (images) et des fichiers usager (scores, préférences).

Fonctionne aussi bien en lançant les sources depuis n'importe quel dossier
qu'avec un exécutable PyInstaller (--onefile), où les ressources sont
extraites dans un dossier temporaire (sys._MEIPASS) qui est effacé à la sortie.
"""

import os
import sys

FIGE = getattr(sys, 'frozen', False)

# Dossier contenant les ressources embarquées (images)
DOSSIER_BASE = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


def ressource(chemin_relatif):
    """Chemin absolu d'une ressource livrée avec le jeu (ex : 'images/pomme.png')"""
    return os.path.join(DOSSIER_BASE, chemin_relatif)


def _dossier_usager():
    """Dossier où sont enregistrés scores et préférences"""
    if not FIGE:
        # Depuis les sources : on garde le dossier usager/ du projet
        return os.path.join(DOSSIER_BASE, 'usager')
    # Exécutable : dossier de données de l'utilisateur (le dossier de l'exécutable
    # n'est pas forcément accessible en écriture, ex : application macOS)
    if sys.platform == 'win32':
        racine = os.environ.get('APPDATA', os.path.expanduser('~'))
        return os.path.join(racine, 'SnakeByte')
    if sys.platform == 'darwin':
        return os.path.expanduser('~/Library/Application Support/SnakeByte')
    racine = os.environ.get('XDG_DATA_HOME', os.path.expanduser('~/.local/share'))
    return os.path.join(racine, 'snakebyte')


def fichier_usager(nom):
    """Chemin absolu d'un fichier usager ('hiscore' ou 'prefs'), dossier créé si besoin"""
    dossier = _dossier_usager()
    os.makedirs(dossier, exist_ok=True)
    return os.path.join(dossier, nom)
