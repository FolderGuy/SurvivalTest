#PRESS D TO ACTIVATE/DEACTIVATE DEBUG MODE

#Configures directories
import os
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data\\")
os.makedirs(data_dir, exist_ok=True) #Creates the data directory
log_dir = os.path.join(main_dir, "logs\\")
os.makedirs(log_dir, exist_ok=True) #Creates the log directory

from datetime import datetime as dt

#Configures Logging
import logging as l
formatted_date = dt.now().strftime("%Y-%m-%d-%H-%M-%S")
log_file_name = formatted_date + ".log"
l.basicConfig(filename= log_dir + log_file_name, level=l.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - line %(lineno)d  - %(message)s',datefmt='%H:%M:%S')


screen_width = 200
screen_height = 200
#Initializes Pygame
try:
	import pygame as pg
except ImportError:
	l.critical("Pygame Import failed")

#Checks if pygame initiated correctly
try:
	pg.init()
	#Sets Screen and Caption
	screen = pg.display.set_mode((screen_width, screen_height), pg.SCALED)
	pg.display.set_caption("Survival Test")
except pygame.error:
	l.critical(pygame.error)

import game_logic

#Starts game
try:
	game_logic.main_loop()
except Exception as e:
	l.critical(f"Can't start game, Error: {e}")

pg.quit()