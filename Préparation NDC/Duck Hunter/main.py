# Pyxel Studio

import pyxel
from random import randint

TITLE = "Snake"
WIDTH = 800
HEIGHT = 800
CASE = 16
pyxel.init(WIDTH, HEIGHT, title=TITLE, fps=3)

duck = [0, 0]

# Variables de direction
DROITE = (1,0)
GAUCHE = (-1, 0)
HAUT = (0, -1)
BAS = (0, 1)
GAUCHE_HAUT = (-1, -1)
DROITE_HAUT = (1, -1)
GAUCHE_BAS = (-1, 1)
DROITE_BAS = (1, 1)

direction = DROITE

def draw():
    pyxel.cls(0)
    pyxel.rect(duck[0] * CASE, duck[1] * CASE, CASE, CASE, 2)
    
    
def update():
    global duck, direction
    directions = [(0, 0), DROITE, GAUCHE, HAUT, BAS, GAUCHE_HAUT, DROITE_HAUT, GAUCHE_BAS, DROITE_BAS]
    
    random = randint(1, 8)
    direction = directions[random]
    
    while (duck[0] + direction[0]) <= 1 and (duck[1] + direction[1]) <= 1:
        random = randint(1, 8)
        direction = directions[random]
    
    duck = [duck[0] + direction[0], duck[1] + direction[1]]

pyxel.run(update, draw)