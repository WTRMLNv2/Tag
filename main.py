import pygame
from pathlib import Path
from screens.start_screen import start_screen
from screens.controls_screen import controls_screen
from screens.map_selection import map_selection_screen
from game.core import run_game

base_path = Path(__file__).parent


def main():
    pygame.init()
    screen = pygame.display.set_mode((1300, 640))
    pygame.display.set_caption("Tag Game")

    start_screen(screen)
    controls_screen(screen)
    selected_map = map_selection_screen(screen)

    while True:
        run_game(screen, selected_map)

if __name__ == "__main__":
    main()