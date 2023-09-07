#PRESS D TO ACTIVATE/DEACTIVATE DEBUG MODE

import logging as l
import pygame as pg
import os
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data\\")
log_dir = os.path.join(main_dir, "logs\\")

debug_mode = False

black = (0, 0, 0)
white = (255, 255, 255)
light_gray = (173, 170, 168)
gray = (57,61,71)
green = (0, 111, 70)
s_green = (3, 160, 98)
red = (217, 33, 33)
blue = (0, 132, 160)
deep_blue = (65, 71, 192)

screen_width, screen_height = 200, 200
screen = pg.display.set_mode((screen_width, screen_height), pg.SCALED)

#Configures cells
cell_size = 20  # Size of each grid cell
rows = screen_height // cell_size
cols = screen_width // cell_size
grid = [[[0, 0] for _ in range(cols)] for _ in range(rows)]

def get_cell_color(row, col):
	val1 = grid[row][col][0]
	color_ret = {
	0 : white,
	1 : black,
	2 :	green,
	3 : red,
	4 : blue,
	5 : deep_blue
	}
	return color_ret.get(val1, s_green)

def draw_biome(biome):
	pass

def draw_cells():
	for row in range(rows):
		for col in range(cols):
			cell_color = get_cell_color(row, col)
			cell_x = col * cell_size
			cell_y = row * cell_size
			pg.draw.rect(screen, cell_color, (cell_x, cell_y, cell_size, cell_size))

			#Draws values, debug
			if debug_mode == True:
				value1, value2 = grid[row][col]
				value1_str = str(value1)
				value2_str = str(value2)
				
				font = pg.font.Font(None, 14)

				value1_surface = font.render(value1_str, True, (0, 0, 0))
				value2_surface = font.render(value2_str, True, (0, 0, 0))

				# Calculate the positions to center the values
				value1_x = cell_x + (cell_size - value1_surface.get_width()) // 2
				value1_y = cell_y + (cell_size - value1_surface.get_height()) // 2

				value2_x = cell_x + 6 + (cell_size - value2_surface.get_width()) // 2
				value2_y = cell_y + (cell_size - value2_surface.get_height()) // 2

				# Blit (draw) the value surfaces onto the screen
				screen.blit(value1_surface, (value1_x, value1_y))
				screen.blit(value2_surface, (value2_x, value2_y))


#main loop
def main_loop():
	global debug_mode

	running = True
	g_pr = False #Handles if the grid was printed to cmd before
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
			if event.type == pg.KEYDOWN and event.key == pg.K_d:
				if debug_mode == False:
					debug_mode = True
					print("DEBUG MODE ACTIVATED")
					l.debug("DEBUG MODE ACTIVATED")
				elif debug_mode == True:
					debug_mode = False
					print("DEBUG MODE DEACTIVATED")
					l.debug("DEBUG MODE DEACTIVATED")

		screen.fill((black)) #Clears the screen

		if g_pr == False:
			try:
				print(grid)
				l.debug('Grid updated')
				g_pr = True
			except Exception as e:
				print(e)

		grid[0][0] = [2, 0]

		draw_biome("Meadow")
		draw_cells()#Draws all the cells

		if debug_mode == True:
			# Draw horizontal lines to separate rows
			for row in range(rows + 1):
				pg.draw.line(screen, gray, (0, row * cell_size), (screen_width, row * cell_size))

			# Draw vertical lines to separate columns
			for col in range(cols + 1):
				pg.draw.line(screen, gray, (col * cell_size, 0), (col * cell_size, screen_height))


		pg.display.flip()