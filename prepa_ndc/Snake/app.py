import pyxel
from random import randint

# Initialisation
TITLE = "Snake"
WIDTH = 240
HEIGHT = 240
CASE = 16
pyxel.init(WIDTH, HEIGHT, title=TITLE, fps=3)
pyxel.load("res.pyxres")

# Variables utilisateurs
snake = [[3,3], [2,3], [1,3]]
score = 0
pomme = [8,3]

# Variables de direction
DROITE = (1,0)
GAUCHE = (-1, 0)
HAUT = (0, -1)
BAS = (0, 1)
direction = DROITE

# Dessin
def draw():
    global direction
    pyxel.cls(0)
    # Pour chaque anneau, dessiner les anneaux, sauf la tête
    for anneau in snake[1:]:
        x, y = anneau[0], anneau[1]
        pyxel.blt(x * CASE, y * CASE, 0, 0, 0, CASE, CASE)
    # Dessiner la tête du serpent
    x_head, y_head = snake[0]
    if direction == HAUT:
        pyxel.blt(x_head * CASE, y_head * CASE, 0, 16, 16, CASE, CASE)
    elif direction == BAS:
        pyxel.blt(x_head * CASE, y_head * CASE, 0, 16, 16, CASE, -CASE)
    elif direction == GAUCHE:
        pyxel.blt(x_head * CASE, y_head * CASE, 0, 16, 0, -CASE, CASE)
    elif direction == DROITE:
        pyxel.blt(x_head * CASE, y_head * CASE, 0, 16, 0, CASE, CASE)
    # Dessiner le score utilisateur
    pyxel.text(4,4,f"SCORE : {score}", 7)
    # Dessiner la pomme
    x_pomme, y_pomme = pomme
    pyxel.blt(x_pomme * CASE, y_pomme * CASE, 0, 32, 0, CASE, CASE)
    
def update():
    # Faire bouger le serpent
    global direction, pomme, score
    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    
    # Si la tête du serpent touche les limites x de l'écran, alors le réapparaitre à l'autre bout.
    # if head[0] >= WIDTH/CASE:
        # head[0] = 0
    # elif head[0] < 0:
        # head[0] = (WIDTH/CASE) - 1
        
    # Si la tête du serpent touche les limites y de l'écran, alors le réapparaitre à l'autre bout.
    # if head[1] >= HEIGHT/CASE:
        # head[1] = 0
    # elif head[1] < 0:
        # head[1] = (HEIGHT/CASE) - 1
    
    if head in snake[2:] or head[1] >= HEIGHT/CASE or head[1] < 0 or head[0] >= WIDTH/CASE or head[0] < 0:
        pyxel.quit()
        
    snake.insert(0, head)
    if head == pomme:
        score += 1
        while pomme in snake:
            pomme = [randint(0, int(WIDTH/CASE) - 1), randint(0, int(HEIGHT/CASE) - 1)]
    else:
        snake.pop()
    
    # Ecouter les actions de l'utilisateurs
    if pyxel.btn(pyxel.KEY_ESCAPE):
        exit()
    elif pyxel.btn(pyxel.KEY_DOWN) and direction in (GAUCHE, DROITE):
        direction = BAS
    elif pyxel.btn(pyxel.KEY_UP) and direction in (GAUCHE, DROITE):
        direction = HAUT
    elif pyxel.btn(pyxel.KEY_LEFT) and direction in (HAUT, BAS):
        direction = GAUCHE
    elif pyxel.btn(pyxel.KEY_RIGHT) and direction in (HAUT, BAS):
        direction = DROITE
    

pyxel.run(update, draw)