import pygame
from math import sqrt
from managers.Subject import Subject

class Gate:
    def __init__(self, x0, y0, xf, yf, tam):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0
        self.y1 = y0 - tam
        self.xf = xf
        self.yf = yf
        self.current_x = self.x1
        self.current_y = self.y1
        self.tam = tam
        self.on = False
        self.on_buffer = False
        self.end_animation = 0

    def draw(self, window, current_frame):
        print("gate.draw")

        step = 59

        if self.on!= self.on_buffer:
            self.end_animation = current_frame + step
            self.on_buffer = self.on

        if current_frame < self.end_animation:
            delta_x = ((self.xf - self.x0)/step) * ((step - self.end_animation + current_frame) if self.on else (self.end_animation - current_frame))
            delta_y = sqrt((self.tam**2) - (delta_x**2))

            y = (self.y0 - delta_y)

            x = (self.x0 + delta_x)

            pygame.draw.line(window, (255, 255, 255), (self.x0, self.y0), (x, y))
        else:
            pygame.draw.line(window, (255, 255, 255), (self.x0, self.y0), (self.current_x, self.current_y))

    def set_on(self, on):
        self.on = on

        if self.on:
            self.current_x = self.xf
            self.current_y = self.yf
        else:
            self.current_x = self.x1
            self.current_y = self.y1

class GateManager(Subject):
    def __init__(self):
        super().__init__()
        self.mode = 0
        self.gates : list[Gate] = []

    def add(self, x0, y0, xf, yf):
        tam = sqrt((x0 - xf) ** 2 + (y0 - yf) ** 2)
        self.gates.append(Gate(x0, y0, xf, yf, tam))

    def set_mode(self, new_mode):
        self.mode = new_mode

        if self.mode == 0:
            self.gates[0].set_on(False)
            self.gates[1].set_on(False)
        elif self.mode == 1:
            self.gates[0].set_on(True)
            self.gates[1].set_on(False)
        else:
            self.gates[0].set_on(False)
            self.gates[1].set_on(True)


    def on_draw(self, data):
        for gate in self.gates:
            gate.draw(data['window'], data['current_frame'])

