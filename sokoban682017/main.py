from gamecontrollers.gamecontrollers import GameController
from gameviews.gameviews import GameView
from gamemodels.gamemodel import GameModel
from gameviews.boomview import BoomView

import pygame
pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False

playermodel = GameModel(1, 2)
assert playermodel.x == 1, playermodel.y == 2
playermodel.move(10, 10)
assert playermodel.x == 11, playermodel.y == 12

playerview = GameView(pygame.image.load("images/pusher.png"), screen)
player = GameController(playermodel, playerview)

# boom = GameController(GameModel(50, 50), BoomView(,screen))
counter = 0
boom_animations = [
    pygame.image.load("images/0.png"),
    pygame.image.load("images/1.png"),
    pygame.image.load("images/2.png"),
    pygame.image.load("images/3.png"),
    pygame.image.load("images/4.png"),
    pygame.image.load("images/5.png"),
    pygame.image.load("images/6.png")]

boom = BoomView(boom_animations, screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))
    player.counter += 1
    if player.counter >= 10:
        player.move(1, 0)
        player.counter = 0
    player.draw()
    boom.draw()
    pygame.display.flip()