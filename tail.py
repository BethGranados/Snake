import actor

#The tail of the snake.
class tail(actor.actor):
    #The tail of the snake follows the otherActor. The otherActor should either be the
    #part of the tail in front of this part, or the head of the snake.
    def follow(self, otherActor):
        self.cord = otherActor.location()
