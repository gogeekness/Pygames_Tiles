'''
# Tile Config, Globals

This file contains the main settings for the program.
All of the colors, tile states, test array offset lists, and main file directories

'''
import os

displaysize = width, height = 1200, 800  # set size of the field

''' RGB colors '''
black = (  0,   0,   0)
white = (255, 255, 255)
dgrey = ( 50,  50,  50)
grey  = (170, 170, 170)
lgrey = (180, 180, 180)
red   = (255,   0,   0)
green = (  0,  255,  0)
blue  = (  0,    0,255)

# define where data directory is located
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data_dir")

tilecolor = ['blank', 'red', 'green', 'blue', 'yellow', 'cyan', 'purple', 'brown', 'grey']
tilestatus = ['init', 'in-play', 'moving', 'new', 'remove']
mousedir = ['north', 'east', 'south', 'west', 'still']
Tilesize = 100  #image size and tile size
Boardersize = 50
speed = 0
boardbuffer = 3
boardsize = (7, 7)  # Active board size
fullboardsize = (boardsize[0] + boardbuffer * 2, boardsize[1] + boardbuffer * 2) # True board size with buffer zone added

''' Patter offsets to test matching color for the group '''
pattern1s = [(0, 0), (0, 1), (0, 2)]
pattern3l = [[(0, -2), (0, -1), (0, 0)], [(0, -1), (0, 0), (0, 1)], [(0, 0), (0, 1), (0, 2)],[(-2, 0), (-1, 0), (0, 0)], [(-1, 0), (0, 0), (1, 0)], [(0, 0), (1, 0), (2, 0)]]
pattern4l = [[(0, -2), (0, -1), (0, 0), (0, 1)], [(0, -1), (0, 0), (0, 1), (0, 2)], [(-2, 0), (-1, 0), (0, 0), (1, 0)],
             [(-1, 0), (0, 0), (1, 0), (2, 0)]]
pattern4s = [[(0, 1), (0, 0), (1, 0), (1, 1)], [(0, 0), (-1, 1), (-1, 0), (0, 1)], [(-1, -1), (-1, 0), (0, -1), (0, 0)],
             [(1, -1), (1, 0), (0, -1), (0, 0)]]
pattern5l = [[(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)], [(0, -2), (0, -1), (0, 0), (0, 1), (0, 2)]]
