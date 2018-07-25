# Tile Config, Globals

# set size of the field
displaysize = width, height = 1200, 800
black = (  0,   0,   0)
white = (255, 255, 255)
dgrey = ( 50,  50,  50)
grey  = (170, 170, 170)
lgrey = (180, 180, 180)
red   = (255,   0,   0)
green = (  0,  255,  0)
blue  = (  0,    0,255)
tilecolor = ['blank', 'red', 'green', 'blue', 'yellow', 'cyan', 'purple', 'brown', 'grey']
tilestatus = ['init', 'in-play', 'moving', 'new', 'remove']
speed = 0
boardbuffer = 3
boardsize = (7, 7)
fullboardsize = (boardsize[0] + boardbuffer * 2, boardsize[1] + boardbuffer * 2)
pattern1s = [(0, 0), (0, 1), (0, 2)]
pattern3l = [[(0, -2), (0, -1), (0, 0)], [(0, -1), (0, 0), (0, 1)], [(0, 0), (0, 1), (0, 2)],[(-2, 0), (-1, 0), (0, 0)], [(-1, 0), (0, 0), (1, 0)], [(0, 0), (1, 0), (2, 0)]]
pattern4l = [[(0, -2), (0, -1), (0, 0), (0, 1)], [(0, -1), (0, 0), (0, 1), (0, 2)], [(-2, 0), (-1, 0), (0, 0), (1, 0)],
             [(-1, 0), (0, 0), (1, 0), (2, 0)]]
pattern4s = [[(0, 1), (0, 0), (1, 0), (1, 1)], [(0, 0), (-1, 1), (-1, 0), (0, 1)], [(-1, -1), (-1, 0), (0, -1), (0, 0)],
             [(1, -1), (1, 0), (0, -1), (0, 0)]]
pattern5l = [[(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)], [(0, -2), (0, -1), (0, 0), (0, 1), (0, 2)]]
