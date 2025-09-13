from managers.Subject import Subject
from managers.CowManager import CowManager
from managers.GateManager import GateManager

class LogicManager(Subject):
    def __init__(self, window_width, window_height, cow_manager: CowManager, gate_manager: GateManager):
        super().__init__()
        self.cow_manager = cow_manager
        self.window_width = window_width
        self.window_height = window_height
        self.gate_manager = gate_manager

    def on_increase_second(self, data):
        print('LogicManager.on_increase_second')
        current_time = data['current_time']

        for cow in self.cow_manager.cows:
            if cow.y + cow.velocity + cow.height <= self.window_height:
                cow.move('down')
            else:
                cow.set_visibility(False)

        if current_time == 1 or current_time%20 == 0:
            self.cow_manager.add(self.window_width)

