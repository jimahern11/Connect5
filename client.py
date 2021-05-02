import socket
import numpy as np
import math
from network import Network
import pygame as py
from pygame_functions import *

width = 500
height = 500
win = py.display.set_mode((width, height))

#name = input("please enter your name.")

#print(f"Hi {name} are you ready to play connect 5")
#py.display.set_caption(f"Hi {name} are you ready to play connect 5")
py.display.set_caption("Connect 5   ")
clientNumber = 0
print("Number of connections ", clientNumber)
####adding to github!!!!!!!!!!!!!!!!!!!!!!


class Player():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.val = 3

    def move(self):
        keys = py.key.get_pressed()

        if keys[py.K_LEFT]:
            self.x -= self.val
        if keys[py.K_RIGHT]:
            self.x += self.val
        if keys[py.K_UP]:
            self.y -= self.val
        if keys[py.K_DOWN]:
            self.y += self.val
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def redrawWindow(win, player, player2):
        win.fill((255, 255, 255))
        player.draw(win)
        player2.draw(win)
        py.display.update()

    def draw(self, win):
        py.draw.rect(win, self.colour, self.rect)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def draw(self, win):
    py.draw.rect(win, self.colour, self.rect)


def move(self):
    keys = py.key.get_pressed()

    if keys[py.K_LEFT]:
        self.x -= self.val
    if keys[py.K_RIGHT]:
        self.x += self.val
    if keys[py.K_UP]:
        self.y -= self.val
    if keys[py.K_DOWN]:
        self.y += self.val
    self.update()


def update(self):
    self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    py.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (0, 255, 0))

    while run:
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                py.quit()
            p.move()
            redrawWindow(win, p, p2)


main()
