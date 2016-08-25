#class that handles the main game loop

import pygame
from gameViewObj import *
from actor import *
from food import *
from player import *
from tail import *


class engine:
    #MainLoop sets up the default values to all of our variables and runs event(), update() and render()
    def mainLoop(self):
        self.scene = gameViewObj()
        self.timer = 0
        self.moveTimer = 3
        self.actorList = [food(400, 600), player(500, 200), tail(900, 900)]
        self.amount = 3

        self.gameOpen = True
        
        self.running = True
        while self.gameOpen:
            #Main Loop for the actual game
            while self.running:
                self.events()
                self.update()
                self.scene.render(self.actorList, self.amount)
                self.scene.drawText("Score: " + str(self.amount - 3) , (0,0))
                self.scene.flippingTheScene()
            #We only exit the loop when we die. All the following is the code for the game over screen.
            self.scene.drawText("Game Over", (300, 320))
            self.scene.drawText("Press Space to play again", (180, 350))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOpen = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.actorList[1].relocate((200, 200))
                        for x in range (self.amount - 1, 2, -1):
                            del self.actorList[x]
                        self.running = True
                        self.amount = 3
            self.scene.flippingTheScene()
    #Event() handles all player input.
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameOpen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.actorList[1].getDirY() != 0:
                        self.actorList[1].changeDirX(-10)
                        self.actorList[1].changeDirY(0)
                if event.key == pygame.K_RIGHT:
                    if self.actorList[1].getDirY() != 0:
                        self.actorList[1].changeDirX(10)
                        self.actorList[1].changeDirY(0)
                if event.key == pygame.K_DOWN:
                    if self.actorList[1].getDirX() != 0:
                        self.actorList[1].changeDirY(10)
                        self.actorList[1].changeDirX(0)
                if event.key == pygame.K_UP:
                    if self.actorList[1].getDirX() != 0:
                        self.actorList[1].changeDirY(-10)
                        self.actorList[1].changeDirX(0)
    #update handles all the interactions between gameObjects (Such as player and food)
    def update(self):
        if(self.timer == self.moveTimer):
            y = self.amount - 1
            for x in range(y, 1, -1):
                self.actorList[x].follow(self.actorList[x - 1])
            self.actorList[1].move()
            self.timer = 0
        self.timer += 1
        if self.actorList[1].collide(self.actorList[0]):
            self.actorList[0].relocate()
            self.actorList.append(tail(900, 900))
            self.amount += 1
        if self.scene.outBoundsLeft(self.actorList[1]) or self.scene.outBoundsRight(self.actorList[1]) or self.scene.outBoundsTop(self.actorList[1]) or self.scene.outBoundsBottom(self.actorList[1]):
            self.running = False
        for x in range(self.amount - 1, 1, -1):
            if self.actorList[1].collide(self.actorList[x]):
                self.running = False
