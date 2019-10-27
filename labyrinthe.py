#-*- utf8 -*-
#import os
import json
import pygame
from pygame.locals import *
from constants import *
import classMove

labyUn = classMove.Laby()
labyUn = labyUn.lab

labyList = list(labyUn)

i = 0
x_mur = []
y_mur = []
nbr_mur = 0
liste_mur = []
span = 43
while i < 225:
	if labyList[i] == "o":
		print(i)
		liste_mur.append(i)
		nbr_mur += 1
		i += 1
		if i <= 15:
			print("inferieur à 15")
			x_mur.append(i * 43 - 43)
			y_mur.append(0)
		if i > 15 and i <= 30:
			print("entre 15 et 30")
			x_mur.append(((i - 15) * 43) - 43)
			y_mur.append(1 * span)
		if i > 30 and i <= 45:
			print("entre 30 et 45")
			x_mur.append(((i - 30) * 43) - 43)
			y_mur.append(2 * span)
		if i > 45 and i <= 60:
			print("entre 45 et 60")
			x_mur.append(((i - 45) * 43) - 43)
			y_mur.append(3 * span)
		if i > 60 and i <= 75:
			print("entre 60 et 75")
			x_mur.append(((i - 60) * 43) - 43)
			y_mur.append(4 * span)
		if i > 75 and i <= 90:
			print("entre 75 et 90")
			x_mur.append(((i - 75) * 43) - 43)
			y_mur.append(5 * span)
		if i > 90 and i <= 105:
			print("entre 90 et 105")
			x_mur.append(((i - 90) * 43) - 43)
			y_mur.append(6 * span)
		if i > 105 and i <= 120:
			print("entre 105 et 120")
			x_mur.append(((i - 105) * 43) - 43)
			y_mur.append(7 * span)
		if i > 120 and i <= 135:
			print("entre 120 et 135")
			x_mur.append(((i - 120) * 43) - 43)
			y_mur.append(8 * span)
		if i > 135 and i <= 150:
			print("entre 135 et 150")
			x_mur.append(((i - 135) * 43) - 43)
			y_mur.append(9 * span)
		if i > 150 and i <= 165:
			print("entre 150 et 165")
			x_mur.append(((i - 150) * 43) - 43)
			y_mur.append(10 * span)
		if i > 165 and i <= 180:
			print("entre 165 et 180")
			x_mur.append(((i - 165) * 43) - 43)
			y_mur.append(11 * span)
		if i > 180 and i <= 195:
			print("entre 180 et 195")
			x_mur.append(((i - 180) * 43) - 43)
			y_mur.append(12 * span)
		if i > 195 and i <= 210:
			print("entre 195 et 210")
			x_mur.append(((i - 195) * 43) - 43)
			y_mur.append(13 * span)
		if i > 210 and i <= 225:
			print("entre 210 et 225")
			x_mur.append(((i - 210) * 43) - 43)
			y_mur.append(14 * span)
	else:
		i += 1
print(liste_mur)
print(x_mur)
print(y_mur)


fenetre = pygame.display.set_mode((640, 640))

fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))


perso = pygame.image.load("macGyver.png").convert_alpha()
position_perso = perso.get_rect()

position_perso.center = 59, 64
fenetre.blit(perso, (position_perso))
gardien = pygame.image.load("Gardien.png").convert_alpha()

mur = pygame.image.load("mur.png").convert_alpha()
position_mur = mur.get_rect()
position_mur.center = 43, 43


pygame.display.flip()

keep = 1

pygame.key.set_repeat(400, 30)

while keep:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				position_perso = position_perso.move(0,43)
			if event.key == K_UP:
				position_perso = position_perso.move(0,-43)		
			if event.key == K_RIGHT:
				position_perso = position_perso.move(43,0)
			if event.key == K_LEFT:
				position_perso = position_perso.move(-43,0)
		if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
			print("zone dangereuse")

	fenetre.blit(fond, (0,0))
	fenetre.blit(gardien, (100,100))
	
	index_mur_x = 0
	index_mur_y = 0

	while index_mur_x < len(x_mur):
		for x in x_mur:
			x = x_mur[index_mur_x]
			index_mur_x += 1
			y = y_mur[index_mur_y]
			index_mur_y += 1
			fenetre.blit(mur, (x,y))
		
	
	
	fenetre.blit(perso, position_perso)
	pygame.display.flip()
	"""
	if position_perso.colliderect(position_mur):
		collision = 1
		print("collision")
	else:
		collision = 0
		print("no collision")
		"""
#os.system("pause")	