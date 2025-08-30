# Pyxel Studio

import pyxel

TITLE = "Animation"
WIDTH = 160
HEIGHT = 128
pyxel.init(WIDTH, HEIGHT, TITLE, fps=20)
pyxel.load("res.pyxres")

player_frames = {
    "right": [[0, 8], [16, 8], [32, 8], [48, 8]],
    "left": [[64, 8], [80, 8], [96, 8], [112, 8]]
}
current_player_frame = [0, player_frames["right"][0]]
player = [16, 64]

def get_camera_pos():
    if player[0] > 16:
        return (player[0] - 16, 0)
    else:
        return (0, 0)

def animate(frames: list):
    global current_player_frame

    if current_player_frame[0] >= len(frames) - 1:
        current_player_frame = [0, frames[0]]
    else:
        i = current_player_frame[0] + 1
        current_player_frame = [i, frames[i]]

def update():
    global player
    
    if pyxel.btn(pyxel.KEY_RIGHT):
        player[0] += 1
        animate(player_frames["right"])
    elif pyxel.btn(pyxel.KEY_LEFT):
        player[0] -= 1
        animate(player_frames["left"])
        
    print(pyxel.pget(player[0], player[1] - 8))
        
    camera = get_camera_pos()
    pyxel.camera(camera[0], camera[1])
        
        
def draw():
    global current_player_frame, player
    pyxel.cls(0)
    
    camera_x, camera_y = get_camera_pos()
    pyxel.bltm(camera_x, camera_y, 0, camera_x, camera_y, pyxel.width, pyxel.height)
    pyxel.blt(player[0], player[1], 0, current_player_frame[1][0], current_player_frame[1][1], 16, 16, 5)

pyxel.run(update, draw)