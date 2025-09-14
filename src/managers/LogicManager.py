from managers.Subject import Subject
from managers.CowManager import CowManager
from managers.GateManager import GateManager
from managers.WallManager import WallManager

class LogicManager(Subject):
    def __init__(self, window_width, window_height, cow_manager: CowManager, gate_manager: GateManager, wall_manager: WallManager):
        super().__init__()
        self.cow_manager = cow_manager
        self.window_width = window_width
        self.window_height = window_height
        self.gate_manager = gate_manager
        self.wall_manager = wall_manager

    def on_increase_second(self, data):
        print('LogicManager.on_increase_second')
        current_time = data['current_time']

        if current_time == 1 or not self.cow_manager.cows[-1].visible:
            self.cow_manager.add(self.window_width)

        cow = self.cow_manager.cows[-1]

        self.gate_manager.set_mode(cow.mark)

        if cow.y <= self.window_height:
            if cow.y > self.wall_manager.walls[0].y1:
                if cow.mark == 1:
                    cow.move('left')
                elif cow.mark == 2:
                    cow.move('right')
                else:
                    cow.move('down')
            else:
                cow.move('down')
        else:
            cow.set_visibility(False)


