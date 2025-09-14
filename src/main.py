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
    logic_manager = LogicManager(window_width, window_height, cow_manager, gate_manager, wall_manager)

    wall_upper_left = {
        "init_x": window_width/2 - 2 * cow_manager.cow_width,
        "init_y": 0,
        "end_x": window_width/2 - 2 * cow_manager.cow_width,
        "end_y": window_height/2 - 2 * cow_manager.cow_height + 100
    }

    wall_upper_right = {
        "init_x": window_width/2 + 2 * cow_manager.cow_width,
        "init_y": 0,
        "end_x": window_width/2 + 2 * cow_manager.cow_width,
        "end_y": window_height/2 - 2 * cow_manager.cow_height + 100
    }

    wall_down_left = {
        "init_x": window_width/2 - 2 * cow_manager.cow_width,
        "init_y": window_height/2 + 2 * cow_manager.cow_height + 100,
        "end_x": window_width/2 - 2 * cow_manager.cow_width,
        "end_y": window_height
    }

    wall_down_right = {
        "init_x": window_width/2 + 2 * cow_manager.cow_width,
        "init_y": window_height/2 + 2 * cow_manager.cow_height + 100,
        "end_x": window_width/2 + 2 * cow_manager.cow_width,
        "end_y": window_height
    }

    wall_manager.add(wall_upper_left["init_x"], wall_upper_left["init_y"], wall_upper_left["end_x"], wall_upper_left["end_y"])
    wall_manager.add(wall_upper_right["init_x"], wall_upper_right["init_y"], wall_upper_right["end_x"], wall_upper_right["end_y"])
    wall_manager.add(wall_down_left["init_x"], wall_down_left["init_y"], wall_down_left["end_x"], wall_down_left["end_y"])
    wall_manager.add(wall_down_right["init_x"], wall_down_right["init_y"], wall_down_right["end_x"], wall_down_right["end_y"])


    def get_x(p1, p2, max_y):
        a = (p1[0] - p2[0])/(p1[1] - p2[1])
        b = p1[1] - a * p1[0]
        x = (max_y - b) / a
        return x

    wall_upper_left_diagonal = {
        "init_x": wall_upper_left["end_x"],
        "init_y": wall_upper_left["end_y"],
        "end_x": get_x((wall_upper_right["end_x"], wall_upper_right["end_y"] - abs(wall_upper_right["end_y"] - wall_down_right["init_y"])), (wall_upper_left["end_x"], wall_upper_left["end_y"]), window_height),
        "end_y": window_height
    }

    wall_upper_right_diagonal = {
        "init_x": wall_upper_right["end_x"],
        "init_y": wall_upper_right["end_y"],
        "end_x": get_x((wall_upper_left["end_x"], wall_upper_left["end_y"] - abs(wall_upper_left["end_y"] - wall_down_left["init_y"])), (wall_upper_right["end_x"], wall_upper_right["end_y"]), window_height),
        "end_y": window_height
    }

    wall_down_left_diagonal = {
        "init_x": wall_down_left["init_x"],
        "init_y": wall_down_left["init_y"],
        "end_x": get_x((wall_upper_right["end_x"], wall_upper_right["end_y"]), (wall_down_left["init_x"], wall_down_left["init_y"]), window_height),
        "end_y": window_height
    }

    wall_down_right_diagonal = {
        "init_x": wall_down_right["init_x"],
        "init_y": wall_down_right["init_y"],
        "end_x": get_x((wall_upper_left["end_x"], wall_upper_left["end_y"]), (wall_down_right["init_x"], wall_down_right["init_y"]), window_height),
        "end_y": window_height
    }

    wall_manager.add(wall_upper_left_diagonal["init_x"], wall_upper_left_diagonal["init_y"], wall_upper_left_diagonal["end_x"], wall_upper_left_diagonal["end_y"])
    wall_manager.add(wall_upper_right_diagonal["init_x"], wall_upper_right_diagonal["init_y"], wall_upper_right_diagonal["end_x"], wall_upper_right_diagonal["end_y"])

    wall_manager.add(wall_down_left_diagonal["init_x"], wall_down_left_diagonal["init_y"], wall_down_left_diagonal["end_x"], wall_down_left_diagonal["end_y"])
    wall_manager.add(wall_down_right_diagonal["init_x"], wall_down_right_diagonal["init_y"], wall_down_right_diagonal["end_x"], wall_down_right_diagonal["end_y"])

    gate_manager.add(wall_down_left["init_x"], wall_down_left["init_y"], wall_upper_right["end_x"], wall_upper_right["end_y"])
    gate_manager.add(wall_down_right["init_x"], wall_down_right["init_y"], wall_upper_left["end_x"], wall_upper_left["end_y"])

    draw_manager.subscribe(cow_manager.on_draw)
    draw_manager.subscribe(wall_manager.on_draw)
    draw_manager.subscribe(gate_manager.on_draw)
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
