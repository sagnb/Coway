import pygame
import random

from managers.Subject import Subject

class Cow:
    def __init__(self, x, y, width, heigh):
        self.x = x
        self.y = y
        self.width = width
        self.height = heigh
        self.velocity = 2
        self.visible = True
        self.mark = random.randint(0, 2)

    def draw(self, window, current_frame):
        print('cow.draw')
        if current_frame >= 0 and self.visible:
            pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move(self, direction):
        inc = int(((self.velocity ** 2)/2) ** 0.5)

        if direction == 'down':
            self.y += self.velocity
        elif direction == 'left':
            self.x -= inc
            self.y += inc
        elif direction == 'right':
            self.x += inc
            self.y += inc

    def set_visibility(self, visibility):
        self.visible = visibility


class CowManager(Subject):
    def __init__(self):
        super().__init__()
        self.cows: list[Cow] = []
        self.cow_width = 50
        self.cow_height = 50

    def add(self, window_width):
        print('CowManager.add')
        self.cows.append(Cow(window_width/2 - self.cow_width/2, 0, self.cow_width, self.cow_height))

        self.notify(self.cows[-1])

    def on_draw(self, data):
        for cow in self.cows:
            cow.draw(data['window'], data['current_frame'])
