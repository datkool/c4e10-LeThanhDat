import pygame
from game.game import Game
from game.map import Map
from game.pusher import Pusher
from game.box import Box
from game.dest import Dest



sokoban = Game()
sokoban.map = Map(10, 10)
sokoban.pusher = Pusher(5, 5)
sokoban.box = Box(8, 3)
sokoban.box2 = Box(1, 8)
sokoban.dest = Dest(3, 3)
sokoban.dest2 = Dest(7, 8)
sokoban.console_draw()

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False
box_image = pygame.image.load("images/box.png")
box2_image = pygame.image.load("images/box2.png")
pusher_image = pygame.image.load("images/pusher.png")
ground_image = pygame.image.load("images/ground.png")
dest_image = pygame.image.load("images/dest.png")
dest2_image = pygame.image.load("images/dest2.png")
sokoban.box.image = box_image
sokoban.box2.image = box2_image
sokoban.dest.image = dest_image
sokoban.dest2.image = dest2_image
sokoban.pusher.image = pusher_image

pixel = 64

# sokoban_undo_pusher = [(sokoban.pusher.x, sokoban.pusher.y)]
# sokoban_undo_box = [(sokoban.box.x, sokoban.box.y)]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        sokoban.handle_input(event)
    sokoban.draw(screen, ground_image)
    pygame.display.flip()
