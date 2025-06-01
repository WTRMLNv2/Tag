import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, settings):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity_y = 0
        self.on_ground = False
        self.speed = settings["speed"]
        self.jump_velocity = settings["jump_velocity"]
        self.gravity = settings["gravity"]
        self.boost_amount = settings["boost_amount"]
        self.max_boosts = settings["max_boosts"]
        self.boosts_available = self.max_boosts
        self.boost_duration = settings["boost_duration"]
        self.last_boost_time = 0
        self.is_boosting = False
        self.boost_end_time = 0
        self.facing_left = False

    def update(self, keys, left, right, up, boost_key):
        current_time = pygame.time.get_ticks()

        if keys[left]:
            self.rect.x -= self.speed
            if not self.facing_left:
                self.image = pygame.transform.flip(self.original_image, True, False)
                self.facing_left = True
        elif keys[right]:
            self.rect.x += self.speed
            if self.facing_left:
                self.image = self.original_image
                self.facing_left = False

        if self.on_ground and keys[up]:
            self.velocity_y = self.jump_velocity
            self.on_ground = False

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.bottom > 640:
            self.rect.bottom = 640
            self.on_ground = True
            self.velocity_y = 0

        if self.is_boosting and current_time >= self.boost_end_time:
            self.speed -= self.boost_amount
            self.is_boosting = False

        if keys[boost_key] and self.boosts_available > 0 and not self.is_boosting:
            self.speed += self.boost_amount
            self.is_boosting = True
            self.boost_end_time = current_time + self.boost_duration
            self.boosts_available -= 1

    def check_platform_collision(self, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.velocity_y = 0
                elif self.velocity_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
