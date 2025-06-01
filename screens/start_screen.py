import pygame
import sys
from pathlib import Path

def start_screen(screen):
    base_path = Path(__file__).parent.parent
    assets_path = base_path / "assets"
    images_path = assets_path / "images"
    background = pygame.image.load(images_path / "Start_Screen.png").convert()
    button_rect = pygame.Rect(500, 370, 300, 90)  # Adjusted for mid-screen

    running = True
    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False

        pygame.display.flip()
