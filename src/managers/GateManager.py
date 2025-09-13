import pygame
from managers.Subject import Subject

class Gate:
    def __init__(self, x0, y0, x1, y1, cow_width, cow_height):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def draw(self, window, current_frame):
        pass

class GateManager(Subject):
    def __init__(self):
        super().__init__()
        pass
