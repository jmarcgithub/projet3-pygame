#-*- coding: utf8 -*-
import pygame
from pygame.locals import *
import constants
import json

#create labyrinthe
class Laby:
	def __init__(self):
		listing = create_maze()
		for a_letter in listing:
			if (a_letter == "_") or (a_letter == "|"):# or (a_letter == "g") or (a_letter == "m"):
				listing = listing.replace(a_letter, "o")
		self.lab = listing
		
def create_maze():
	listing = [] #create empty list
	with open("labyjson.json") as f:
		data = json.load(f) #implement data for read json file
		for entry in data: 
			listing.append(entry["lab01"])#add all line

	listing = "".join(listing)# make chain
	#listing = list(listing)# make list
	return listing
		

#create class Move

class Move:
	def __init__(self):
		self.move = " "
		
			
	