import actor, pygame, random

#The food class. The food is the dots that the snake collects to grow.
class food(actor.actor):
    #Creates the food and puts it in the defined location
    def __init__(self, xCord, yCord):
        self.cord = (xCord, yCord)
        self.image = pygame.Surface(self.size).convert()
        self.image.blit(pygame.image.load("sprite.bmp"), (0,0))
    #Relocate randomly places the dot in the window. It is placed
    #in a 10px grid (Always in a multiple of 10). 
    def relocate(self):
        x = random.randrange(0, 63) * 10
        y = random.randrange(0, 63) * 10
        self.cord = (x, y)
