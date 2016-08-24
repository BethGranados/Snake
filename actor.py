import pygame
class actor:
    size = (10, 10)
    cord = (40, 40)
    #Creates the actor and defined it's location at [XCord, YCord]. Adds a sprite to the actor.
    def __init__(self, xCord, yCord):
        self.cord = (xCord, yCord)
        self.image = pygame.Surface(self.size).convert()
        self.image.blit(pygame.image.load("sprite.bmp"), (0,0))
    #Returns the sprite info for rendering
    def display(self):
        return self.image
    #Returns the location of the sprite
    def location(self):
        return self.cord
    #Relocates the actor to a defined location
    def relocate(self, loc):
        self.cord = loc
    #Returns the size of the actor
    def sizing(self):
        return self.size
    #Determines if the actor is colliding with otherActor
    def collide(self, otherActor):
        if ((self.cord[0] == otherActor.cord[0]) and (self.cord[1] == otherActor.cord[1])):
            return True
        else:
            return False

        
