import pygame
import sys
from pathlib import Path


def map_selection_screen(screen):
    base_path = Path(__file__).parent.parent
    assets_path = base_path / "assets"
    images_path = assets_path / "images"
    background = pygame.image.load(images_path / "Choose map.png").convert()
    map1_rect = pygame.Rect(160, 200, 470, 350)
    map2_rect = pygame.Rect(670, 200, 470, 350)

    font = pygame.font.Font(None, 50)
    map1_text = font.render("Map 1", True, (255, 255, 255))
    map2_text = font.render("Map 2", True, (255, 255, 255))

    running = True
    selected_map = 1

    while running:
        screen.blit(background, (0, 0))
        # screen.blit(map1_text, map1_text.get_rect(center=map1_rect.center))
        # screen.blit(map2_text, map2_text.get_rect(center=map2_rect.center))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if map1_rect.collidepoint(event.pos):
                    selected_map = 1
                    running = False
                elif map2_rect.collidepoint(event.pos):
                    selected_map = 2
                    running = False

        pygame.display.flip()

    return selected_map
