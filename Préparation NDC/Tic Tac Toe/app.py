# Pyxel Studio

import pyxel

TITLE = "TIC TAC TOE"
WIDTH = 49
HEIGHT = 65
CASE = 16
pyxel.init(WIDTH, HEIGHT, title=TITLE, fps=30)
pyxel.load("res.pyxres")

positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
keys_positions = [["A", "Z", "E"], ["Q", "S", "D"], ["W", "X", "C"]]
player = 1
won = 0

def draw():
    global player, won
    players = {1:1, 4:2}
    
    pyxel.cls(0)
    match won:
        case 0:
            pyxel.text(1, 1, f"PLAYER {players[player]}", 7)
        case 1:
            pyxel.text(1, 1, f"P1 won", 7)
            pyxel.text(1, 8, "Space to reset", 7)
        case 4: 
            pyxel.text(1, 1, f"P2 won", 7)
            pyxel.text(1, 8, "Space to reset", 7)
        case -1:
            pyxel.text(1, 1, f"Equality", 7)
            pyxel.text(1, 8, "Space to reset", 7)
    
    pyxel.line(16, 16, 16, 64, 7)
    pyxel.line(32, 16, 32, 64, 7)
    pyxel.line(48, 16, 48, 64, 7)
    pyxel.line(0, 16, 0, 64, 7)
    pyxel.line(0, 16, 48, 16, 7)
    pyxel.line(0, 32, 48, 32, 7)
    pyxel.line(0, 48, 48, 48, 7)
    pyxel.line(0, 64, 48, 64, 7)

    for i in range(len(positions)):
        for j in range(len(positions[i])):
            x, y = (1 + j * 16), (17 + i * 16)
            
            if positions[i][j] == 1:
                # Rond
                pyxel.blt(x, y, 0, 0, 0, 16, 16)
            elif positions[i][j] == 4:
                # Croix
                pyxel.blt(x, y, 0, 16, 0, 16, 16)
            else:
                # Contrôles
                pyxel.text(x + 5.5, y + 4, keys_positions[i][j], 7)


def update():
    global positions, player, won
    
    if won != 0:
        if pyxel.btn(pyxel.KEY_SPACE):
            won = 0
        pass
    
    sum_horizontal = [sum(positions[0]), sum(positions[1]), sum(positions[2])]
    sum_vertical = [sum(p[0] for p in positions), sum(p[1] for p in positions), sum(p[2] for p in positions)]
    sum_diagonal = [(positions[0][0] + positions[1][1] + positions[2][2]), (positions[2][0] + positions[1][1] + positions[0][2])]
    
    sums = sum_horizontal + sum_vertical + sum_diagonal
    sum_1 = [s for s in sums if s == 1 * 3]
    sum_4 = [s for s in sums if s == 4 * 3]
    if len(sum_1) != 0:
        won = 1
        positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        player = 1
        pass
    elif len(sum_4) != 0:
        won = 4
        positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        player = 1
        pass
    
    zeros = [z for z in (positions[0] + positions[1] + positions[2]) if z == 0]
    if len(zeros) == 0:
        won = -1
        positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        player = 1

    coords = []
    if pyxel.btn(pyxel.KEY_A):
        coords = [0, 0]
    elif pyxel.btn(pyxel.KEY_Z):
        coords = [0, 1]
    elif pyxel.btn(pyxel.KEY_E):
        coords = [0, 2]
    elif pyxel.btn(pyxel.KEY_Q):
        coords = [1, 0]
    elif pyxel.btn(pyxel.KEY_S):
        coords = [1, 1]
    elif pyxel.btn(pyxel.KEY_D):
        coords = [1, 2]
    elif pyxel.btn(pyxel.KEY_W):
        coords = [2, 0]
    elif pyxel.btn(pyxel.KEY_X):
        coords = [2, 1]
    elif pyxel.btn(pyxel.KEY_C):
        coords = [2, 2]
    
    if len(coords) != 0 and won == 0:
        y, x = coords
        if positions[y][x] == 0:
            positions[y][x] = player
            player = {1:4,4:1}[player]
            

pyxel.run(update, draw)