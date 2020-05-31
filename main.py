# https://www.youtube.com/watch?v=UejF9X8GyuU&list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2&index=4
# Code from A plus coding


import pygame
import sys
import numpy as np
import time
import sys
from game_window_class import *


WIDTH, HEIGHT = 800, 800
BACKGROUND = (199, 199, 199)
FPS = 60

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)


def update():
    game_window.update()

def draw():
    window.fill(BACKGROUND)
    game_window.draw()

def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < WIDTH -100:
        if pos[1] > 180 and pos[1] < HEIGHT - 20:
            return True
    return False

def click_cell(pos):
    grid_pos = [pos[0]-100, pos[1]-180]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1] // 20


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window, 100, 180)


running = True
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()


