

import pygame

#gameViewObj class handles the display of the game
class gameViewObj:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screenSize = [640, 640]
        self.gameScreen = pygame.display.set_mode(self.screenSize)
        self.frameClock = pygame.time.Clock()
        self.fps = 60
        self.font = pygame.font.SysFont('mono', 24, bold=True)

    #displays the actor on the screen
    def paint(self, actor):
        loc = actor.location()
        dispLoc = (loc[0], loc[1])
        self.gameScreen.blit(actor.display(), dispLoc)

    #takes in a list of actors and uses paint() to display them on the screen.
    def render(self, actorList, amount):
        for x in range(0, amount):
            self.paint(actorList[x])
    #determines if the 
    def outBoundsLeft(self, actor, buff = 0):
        loc = actor.location()
        if( (loc[0] + buff) > self.screenSize[0] - 10):
            return True
        return False
    def outBoundsRight(self, actor, buff = 0):
        loc = actor.location()
        if((loc[0] - buff) < 0):
            return True
        return False
    def outBoundsTop(self, actor, buff = 0):
        loc = actor.location()
        if ((loc[1] + buff) > self.screenSize[1]):
            return True
        return False
    def outBoundsBottom(self, actor, buff = 0):
        loc = actor.location()
        if ((loc[1] - buff) < 0):
            return True
        return False
    def drawText(self, text, loc):
        text = self.font.render(text, True, (255, 255, 255))
        self.gameScreen.blit(text, loc)
        

    def flippingTheScene(self):
        pygame.display.flip()
        self.frameClock.tick(self.fps)
        self.gameScreen.fill([0,0,0])

