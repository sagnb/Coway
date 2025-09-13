import pygame
from managers.Subject import Subject

class Wall:
    def __init__(self, x0, y0, x1, y1):
        super().__init__()
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def draw(self, window, current_frame):
        if current_frame >=0:
            pygame.draw.line(window, (255, 255, 255), (self.x0, self.y0), (self.x1, self.y1))

class WallManager(Subject):
    def __init__(self):
        super().__init__()
        self.walls: list[Wall] = []

    def add(self, x0, y0, x1, y1):
        self.walls.append(Wall(x0, y0, x1, y1))

        self.notify(self.walls[-1])

    def on_draw(self, data):
        for wall in self.walls:
            wall.draw(data['window'], data['current_frame'])
