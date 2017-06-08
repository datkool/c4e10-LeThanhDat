class Pusher:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def collide(self, obj, dx, dy):
        if self.x + dx == obj.x and self.y + dy == obj.y:
            return True
        else:
            return False
