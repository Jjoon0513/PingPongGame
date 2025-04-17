import pygame
from obj.circle import Circle
from system.camera import Camera



class Square:
    color:tuple[int,int,int]
    position:tuple[int,int]
    screen:pygame.display.set_mode()
    width:int
    height:int
    camera: Camera


    def __init__(self, screen_:pygame.display.set_mode(),
                 pos:tuple[int,int],
                 col:tuple[int,int,int],
                 wid:int,
                 hei:int,
                 camera:Camera
                 ):
        self.position = pos
        self.screen = screen_
        self.color = col
        self.width = wid
        self.height = hei
        self.camera = camera


    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0] - self.width / 2 - self.camera.position[0], self.position[1] + self.height / 2 + self.camera.position[1], self.width, self.height))


    def move(self, dx:int = 0, dy:int = 0):
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def check_collision(self, circle_:Circle):

        circle_x, circle_y = circle_.position
        rect_x, rect_y = self.position
        rect_w, rect_h = self.width, self.height

        rect_x -= rect_w / 2

        closest_x = max(rect_x, min(circle_x, rect_x + rect_w))
        closest_y = max(rect_y, min(circle_y, rect_y + rect_h))

        distance = ((circle_x - closest_x) ** 2 + (circle_y - closest_y) ** 2) ** 0.5
        return distance < circle_.radius

    def isoutofscreen(self):
        return self.position[1] + self.camera.position[1] > self.screen.get_size()[1]
