from managers.Subject import Subject

class TimeManager(Subject):
    def __init__(self):
        super().__init__()
        self.current_time = 0

    def increase_second(self, current_frame):
        self.current_time += 1 if current_frame%60 == 0 else 0

        print(f'TimeManager.increase_second current_time = {self.current_time}')

        self.notify({ 'current_time': self.current_time, 'current_frame': current_frame })

