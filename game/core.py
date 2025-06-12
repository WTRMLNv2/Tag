import pygame, random, sys
from game.player import Player #type:ignore
from game.platform import Platform #type:ignore
from game.portal import Portal #type:ignore
from game.settings import * #type:ignore
from pathlib import Path

def run_game(screen, selected_map):

    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000

    base_path = Path(__file__).parent.parent  # Points to your project root (adjust if needed)
    assets_path = base_path / "assets"
    images_path = assets_path / "images"
    sounds_path = assets_path / "sounds"

    # Load assets using pathlib
    bg_snow = pygame.image.load(str(images_path / "Bg_Snow.png")).convert()
    bg_savanna = pygame.image.load(str(images_path / "bg_Savannah.png")).convert()
    red_win = pygame.image.load(str(images_path / "Blue Lose.png"))
    blue_win = pygame.image.load(str(images_path / "Red Lose.png"))
    it_icon = pygame.transform.scale(pygame.image.load(str(images_path / "It_img.png")), (30, 30))

    blue_img = pygame.transform.scale(pygame.image.load(str(images_path / "Blue_player.png")), (26, 30))
    red_img = pygame.transform.scale(pygame.image.load(str(images_path / "Red_player.png")), (26, 30))

    icon_img = pygame.image.load(str(assets_path / "TagLogo.png"))
    pygame.display.set_icon(icon_img)

    tag_sound = pygame.mixer.Sound(str(sounds_path / "pop_sound.mp3"))

    # Pick background and platform layout
    background, platform_list = load_map(selected_map, images_path)


    # Create groups
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    portals = pygame.sprite.Group()

    # Create players
    blue = Player(blue_img, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, player_settings())  #type:ignore
    red = Player(red_img, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, player_settings())    #type:ignore
    players = [blue, red]
    it_player = random.choice(players)


    all_sprites.add(blue, red)

    for platform in platform_list:
        platforms.add(platform)
        all_sprites.add(platform)

    start_time = pygame.time.get_ticks()
    last_tag_time = start_time
    last_portal_spawn = start_time

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        blue.update(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_m)
        red.update(keys, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_t)

        blue.check_platform_collision(platforms)
        red.check_platform_collision(platforms)

        # Spawn portals
        now = pygame.time.get_ticks()
        if now - last_portal_spawn > 30000 and len(portals) == 0:
            portals.add(*spawn_portals(platforms))
            last_portal_spawn = now

        # Handle portal teleport
        for player in [blue, red]:
            for portal in list(portals):
                if portal.active and pygame.sprite.collide_rect(player, portal):
                    player.rect.center = portal.pair.rect.center
                    portal.active = portal.pair.active = False
                    portals.empty()

        # Handle tag logic
        if pygame.sprite.collide_rect(blue, red) and (now - last_tag_time > COOLDOWN_TIME): #type:ignore
            it_player = red if it_player == blue else blue
            tag_sound.play()
            last_tag_time = now

        # Draw everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        portals.draw(screen)
        portals.update(dt)

        it_rect = it_icon.get_rect(center=(it_player.rect.centerx, it_player.rect.top - 20))
        screen.blit(it_icon, it_rect)

        draw_timer(screen, start_time)

        pygame.display.flip()
        clock.tick(60)

        if get_remaining_time(start_time) <= 0:
            running = False

    # Show end screen
    winner_bg = blue_win if it_player == blue else red_win
    screen.blit(winner_bg, (0, 0))
    pygame.display.flip()
    pygame.time.wait(2000)

    font = pygame.font.Font(None, 50)
    text = font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH // 2 + 170, SCREEN_HEIGHT // 2 + 70)) #type:ignore
    pygame.display.flip()

    wait_for_restart()


# ========== Supporting Functions ==========

def load_map(selected_map, images_path):
    if selected_map == 1:
        bg = pygame.image.load(str(images_path / "Bg_Snow.png")).convert()
        platforms = [
            Platform(250, 400, 300, 20, str(images_path / "300.png")), 
            Platform(800, 400, 300, 20, str(images_path / "300.png")),
            Platform(800, 500, 300, 20, str(images_path / "300.png")),
            Platform(100, 300, 200, 20, str(images_path / "200.png")),
            Platform(400, 250, 200, 20, str(images_path / "200.png")),
            Platform(200, 150, 200, 20, str(images_path / "200.png")),
            Platform(50, 500, 200, 20, str(images_path / "200.png")),
            Platform(1001, 199, 200, 20, str(images_path / "200.png")),
            Platform(1100, 300, 200, 20, str(images_path / "200.png")),
            Platform(600, 350, 150, 20, str(images_path / "150.png")),
            Platform(500, 100, 150, 20, str(images_path / "150.png")),
            Platform(600, 200, 150, 20, str(images_path / "150.png")),
            Platform(906, 50, 200, 20, str(images_path / "200.png")),
            Platform(926, -20, 150, 20, str(images_path / "150.png")),
        ]
    else:
        bg = pygame.image.load(str(images_path / "bg_Savannah.png")).convert()
        platforms = [
            Platform(0, 515, 300, 20, str(images_path / "301.png")), 
            Platform(187, 153, 300, 20, str(images_path / "301.png")),  
            Platform(884, 107, 300, 20, str(images_path / "301.png")),  
            Platform(567, 452, 200, 20, str(images_path / "201.png")), 
            Platform(884, 525, 200, 20, str(images_path / "201.png")),  
            Platform(608, 241, 200, 20, str(images_path / "201.png")),  
            Platform(1100, 355, 200, 20, str(images_path / "201.png")),  
            Platform(835, 364, 150, 20, str(images_path / "151.png")), 
            Platform(0, 251, 150, 20, str(images_path / "151.png")),  
            Platform(339, 374, 150, 20, str(images_path / "151.png")),
        ]
    return bg, platforms

def spawn_portals(platforms):
    def get_pos():
        plat = random.choice(platforms.sprites())
        x = random.randint(plat.rect.left + 10, plat.rect.right - 10)
        y = plat.rect.top - 20
        return x, y

    x1, y1 = get_pos()
    x2, y2 = get_pos()
    p1 = Portal(x1, y1)
    p2 = Portal(x2, y2)
    p1.pair = p2
    p2.pair = p1
    return [p1, p2]

def draw_timer(screen, start_time):
    time_left = get_remaining_time(start_time)
    font = pygame.font.Font(None, 40)
    timer = font.render(f"{time_left}s", True, (0, 0, 0))
    screen.blit(timer, (650, 10))

def get_remaining_time(start_time):
    elapsed = (pygame.time.get_ticks() - start_time) // 1000
    return max(0, TIMER_DURATION // 1000 - elapsed) #type:ignore

def wait_for_restart():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return

def player_settings():
    return {
        "speed": 5,
        "jump_velocity": JUMP_VELOCITY, #type:ignore
        "gravity": GRAVITY, #type:ignore
        "boost_amount": SPEED_BOOST_AMOUNT, #type:ignore
        "boost_duration": SPEED_BOOST_DURATION, #type:ignore
        "max_boosts": MAX_SPEED_BOOSTS #type:ignore
    }
