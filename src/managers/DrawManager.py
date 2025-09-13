from managers.Subject import Subject

class DrawManager(Subject):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def draw(self, current_frame):
        self.notify({ 'current_frame': current_frame, 'window': self.window})
