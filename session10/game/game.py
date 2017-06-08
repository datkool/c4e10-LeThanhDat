import pygame

class Game:
    def __init__(self):
        pass
    def console_draw(self):
        for y in range(self.map.height):
            for x in range(self.map.width):
                if y == self.dest.y and x == self.dest.x:
                    print(" D ", end = "")
                elif y == self.box.y and x == self.box.x:
                    print(" B ", end = "")
                elif y == self.pusher.y and x == self.pusher.x:
                    print(" P ", end = "")
                else:
                    print(" - ", end = "")
            print()

    def draw_image_center(self, object, screen):
        pixel = 64
        w = (pixel - object.image.get_width()) / 2 + object.x * pixel
        h = (pixel - object.image.get_height()) / 2 + object.y * pixel
        screen.blit(object.image, (w, h))

    def draw(self, screen, ground_image):
        pixel = 64
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(ground_image, (x * pixel, y * pixel))
        self.draw_image_center(self.dest, screen)
        self.draw_image_center(self.dest2,screen)
        self.draw_image_center(self.box, screen)
        self.draw_image_center(self.box2,screen)
        self.draw_image_center(self.pusher, screen)

    def in_map(self, obj, dx, dy):
        if 0 <= obj.x + dx < self.map.width and 0 <= obj.y + dy < self.map.height:
            return True
        return False

    def check_win(self):
        if self.box.x == self.dest.x and self.box.y == self.dest.y:
            return True
        else:
            return False

    def handle_input(self, event):
        dx = 0
        dy = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    dy -=1
            elif event.key == pygame.K_DOWN:
                    dy += 1
            elif event.key == pygame.K_RIGHT:
                    dx += 1
            elif event.key == pygame.K_LEFT:
                    dx -= 1
            # elif event.key == pygame.K_r:
            #     self.map = Map(10, 10)
            #     self.pusher(5, 5)
            #     self.box(8, 3)
            #     self.dest(3, 3)

        if self.pusher.collide(self.box, dx, dy):
            if self.in_map(self.box, dx, dy):
                self.box.move(dx, dy)
                self.pusher.move(dx, dy)
            else:
                self.pusher.move(dx, dy)

        elif self.in_map(self.pusher, dx, dy):
            self.pusher.move(dx, dy)
