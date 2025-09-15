from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
time = 0
angle = 270

while time < 50:
    clear_canvas_now()
    grass.draw_now(400, 30)

    if(time % 2 == 0):
        character.draw_now(x, y)
        if (x == 780):
            if (90 <= y < 560):
                y = y + 2
            else:
                x = x - 2
        elif (x == 20):
            if (90 < y <= 560):
                y = y - 2
            else:
                x = x + 2
        elif (y == 90):
            x = x + 2
            if (x == 400):
                time = time + 1
        elif (y == 560):
            x = x - 2

    elif (time % 2 == 1):
        prev_angle = angle

        rad = math.radians(angle)
        x = 400 + 210 * math.cos(rad)
        y = 300 + 210 * math.sin(rad)
        character.draw_now(x, y)

        angle = (angle - 1) % 360

        if angle == 270:
            time = time + 1
            x = 400
            y = 90

        delay(0.01)

delay(5)
close_canvas()