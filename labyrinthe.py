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
x_wall = []
y_wall = []
nbr_wall = 0
liste_wall = []
span = 43

# CREATE WALL
while i < 225:
	if labyList[i] == "o":
		liste_wall.append(i)
		nbr_wall += 1
		i += 1
		if i <= 15:
			x_wall.append(i * 43 - 43)
			y_wall.append(0)
		if i > 15 and i <= 30:
			x_wall.append(((i - 15) * 43) - 43)
			y_wall.append(1 * span)
		if i > 30 and i <= 45:
			x_wall.append(((i - 30) * 43) - 43)
			y_wall.append(2 * span)
		if i > 45 and i <= 60:
			x_wall.append(((i - 45) * 43) - 43)
			y_wall.append(3 * span)
		if i > 60 and i <= 75:
			x_wall.append(((i - 60) * 43) - 43)
			y_wall.append(4 * span)
		if i > 75 and i <= 90:
			x_wall.append(((i - 75) * 43) - 43)
			y_wall.append(5 * span)
		if i > 90 and i <= 105:
			x_wall.append(((i - 90) * 43) - 43)
			y_wall.append(6 * span)
		if i > 105 and i <= 120:
			x_wall.append(((i - 105) * 43) - 43)
			y_wall.append(7 * span)
		if i > 120 and i <= 135:
			x_wall.append(((i - 120) * 43) - 43)
			y_wall.append(8 * span)
		if i > 135 and i <= 150:
			x_wall.append(((i - 135) * 43) - 43)
			y_wall.append(9 * span)
		if i > 150 and i <= 165:
			x_wall.append(((i - 150) * 43) - 43)
			y_wall.append(10 * span)
		if i > 165 and i <= 180:
			x_wall.append(((i - 165) * 43) - 43)
			y_wall.append(11 * span)
		if i > 180 and i <= 195:
			x_wall.append(((i - 180) * 43) - 43)
			y_wall.append(12 * span)
		if i > 195 and i <= 210:
			x_wall.append(((i - 195) * 43) - 43)
			y_wall.append(13 * span)
		if i > 210 and i <= 225:
			x_wall.append(((i - 210) * 43) - 43)
			y_wall.append(14 * span)
	else:
		i += 1

fenetre = pygame.display.set_mode((640, 640))

fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))


perso = pygame.image.load("macGyver.png").convert_alpha()
position_perso = perso.get_rect()

position_perso.center = 59, 64
fenetre.blit(perso, (position_perso))
gardien = pygame.image.load("Gardien.png").convert_alpha()

wall = pygame.image.load("mur.png").convert_alpha()
position_wall = wall.get_rect()
position_wall.center = 43, 43


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
	
	index_wall_x = 0
	index_wall_y = 0

	while index_wall_x < len(x_wall):
		for x in x_wall:
			x = x_wall[index_wall_x]
			index_wall_x += 1
			y = y_wall[index_wall_y]
			index_wall_y += 1
			fenetre.blit(wall, (x,y))
		
	
	
	fenetre.blit(perso, position_perso)
	pygame.display.flip()
	
	
		
#os.system("pause")	