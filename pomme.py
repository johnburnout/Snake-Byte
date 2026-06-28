# -*- coding:Utf8 -*-

# ##################
# Snake Byte v1.0  #
#   Jean Roussie   #
# jean@roussie.net #
# ##################

from tkinter import PhotoImage


class Pomme(object):
	"""Classe de Pomme"""
	
	def __init__(self, canevas):
		self.canevas, self.x, self.y = canevas, -100, -100
		
		# Initialisation des variables
		
		self.img_pomme = PhotoImage(file="images/pomme.png")
		
		self.pomme = self.canevas.create_image(self.x, self.y, image=self.img_pomme)
	
	def deplace_pomme(self, x, y):
		""" genération d'une pomme"""
		
		self.x, self.y = x, y
		self.canevas.coords(self.pomme, 20*x-10, 20*y-10)
