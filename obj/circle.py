import pygame
from system.camera import Camera

class Circle:
    color:tuple[int,int,int]
    position:tuple[int,int]
    radius:int
    screen:pygame.display.set_mode()
    camera: Camera

    def __init__(self,
                 screen_:pygame.display.set_mode(),
                 pos:tuple[int,int],
                 col:tuple[int,int,int],
                 rad:int,
                 camera: Camera
                 ):
        self.position = pos
        self.screen = screen_
        self.color = col
        self.radius = rad
        self.camera = camera

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.position[0] - self.camera.position[0], self.position[1] + self.camera.position[1]), self.radius)

    def move(self, dx:int = 0, dy:int = 0):

        self.position = (self.position[0] + dx, self.position[1] + dy)

