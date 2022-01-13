import pygame

import core
from Rocher import Creep
from Joueur import Avatar
from pygame.math import Vector2

def setup():
    print("Setup START----------")

    core.fps = 60
    core.WINDOW_SIZE = [1200, 1000]
    core.memory("a",Avatar())
    core.memory("c",Creep())
    core.memory("listCreep",[])
    core.memory("nbrCreep",50)





    for i in range(0,core.memory("nbrCreep")):
        core.memory("listCreep").append(Creep())
    print("Setup END----------")


def edge():

    if core.memory("a").position.y + core.memory("a").rayon > core.WINDOW_SIZE[1]:
        core.memory("a").position = Vector2(core.memory("a").position.x,core.WINDOW_SIZE[1]-core.memory("a").rayon)

    if core.memory("a").position.x + core.memory("a").rayon > core.WINDOW_SIZE[0]:
        core.memory("a").position = Vector2(core.WINDOW_SIZE[0]-core.memory("a").rayon,core.memory("a").position.y)

    if core.memory("a").position.x - core.memory("a").rayon < 0:
        core.memory("a").position = Vector2(core.memory("a").rayon, core.memory("a").position.y)

    if core.memory("a").position.y - core.memory("a").rayon < 0:
        core.memory("a").position = Vector2(core.memory("a").position.x, core.memory("a").rayon)


def run ():
    core.cleanScreen()


    for creep in core.memory("listCreep"):
        creep.show(core.screen)
        creep.deplacement()
        creep.bordure(core.WINDOW_SIZE)


    core.memory("a").moov(core.getMouseLeftClick())
    edge()
    core.memory("a").show()

    core.memory("a").manger(core.memory("listCreep"))

core.main(setup, run)