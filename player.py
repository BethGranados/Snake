import actor

class player(actor.actor):
    movement = (0, 10)
    def move(self):
        self.cord = (self.cord[0] + self.movement[0], self.cord[1] + self.movement[1])
    def changeDirX(self, x):
        self.movement = (x, self.movement[1])
    def changeDirY(self, y):
        self.movement = (self.movement[0], y)
    def getDirX(self):
        return self.movement[0]
    def getDirY(self):
        return self.movement[1]
    def display(self):
        return self.image
