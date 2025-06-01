import pygame
from pathlib import Path

class Portal(pygame.sprite.Sprite):
    base_path = Path(__file__).parent.parent
    assets_path = base_path / "assets"
    images_path = assets_path / "images"

    def __init__(self, x, y):
        super().__init__()
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(str(self.images_path / f"portal_{i}.png")).convert_alpha(), 
                (30, 30)
            ) for i in range(1, 6)
        ]
        self.current_frame = 0
        self.animation_speed = 0.2  # tweak as needed
        self.frame_timer = 0.0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.pair = None
        self.active = True


    def update(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.animation_speed:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
