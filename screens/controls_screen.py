import pygame
import sys
from pathlib import Path

def controls_screen(screen):
    base_path = Path(__file__).parent.parent
    assets_path = base_path / "assets"
    images_path = assets_path / "images"
    background = pygame.image.load(images_path / "Controls.png").convert()
    button_rect = pygame.Rect(550, 520, 200, 80)
    font = pygame.font.Font(None, 50)
    text = font.render("Continue", True, (255, 255, 255))

    running = True
    while running:
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text, text.get_rect(center=button_rect.center))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False

        pygame.display.flip()
