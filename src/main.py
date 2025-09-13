import pygame
import sys

from managers.CowManager import CowManager
from managers.DrawManager import DrawManager
from managers.GateManager import GateManager
from managers.LogicManager import LogicManager
from managers.TimeManager import TimeManager
from managers.WallManager import WallManager

def main():
    pygame.init()

    window_width, window_height = 800, 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Cow Way")

    clock = pygame.time.Clock()

    time_manager = TimeManager()
    draw_manager = DrawManager(window)
    cow_manager = CowManager()
    wall_manager = WallManager()
    gate_manager = GateManager()
    logic_manager = LogicManager(window_width, window_height, cow_manager, gate_manager)

    wall_manager.add(window_width/2 - 2 * cow_manager.cow_width, 0, window_width/2 - 2 * cow_manager.cow_width, window_height/2 - 2 * cow_manager.cow_height)
    wall_manager.add(window_width/2 - 2 * cow_manager.cow_width, window_height/2 + 2 * cow_manager.cow_height, window_width/2 - 2 * cow_manager.cow_width, window_height)
    wall_manager.add(window_width/2 + 2 * cow_manager.cow_width, 0, window_width/2 + 2 * cow_manager.cow_width, window_height/2 - 2 * cow_manager.cow_height)
    wall_manager.add(window_width/2 + 2 * cow_manager.cow_width, window_height/2 + 2 * cow_manager.cow_height, window_width/2 + 2 * cow_manager.cow_width, window_height)

    wall_manager.add(window_width/2 - 2 * cow_manager.cow_width, window_height/2 - 2 * cow_manager.cow_height, 0, window_height - 3 * cow_manager.cow_height)
    wall_manager.add(window_width/2 - 2 * cow_manager.cow_width, window_height/2 + 2 * cow_manager.cow_height, cow_manager.cow_width, window_height)

    wall_manager.add(window_width/2 + 2 * cow_manager.cow_width, window_height/2 - 2 * cow_manager.cow_height, window_width, window_height - 3 * cow_manager.cow_height)
    wall_manager.add(window_width/2 + 2 * cow_manager.cow_width, window_height/2 + 2 * cow_manager.cow_height, window_width - cow_manager.cow_width, window_height)

    draw_manager.subscribe(cow_manager.on_draw)
    draw_manager.subscribe(wall_manager.on_draw)
    time_manager.subscribe(logic_manager.on_increase_second)

    current_frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_frame += 1
        print(f'current_frame = {current_frame}')

        # update
        time_manager.increase_second(current_frame)

        # clear window
        window.fill((0, 0, 0))

        # draw
        draw_manager.draw(current_frame)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
