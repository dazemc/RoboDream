import pygame
import spritesheet, fighter

pygame.init()

FPS = 60
CLOCK = pygame.time.Clock()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Robo Dream")
update_time = pygame.time.get_ticks()

# BGM
BGM = pygame.mixer.Sound("BGM/2019-01-10_-_Land_of_8_Bits_-_Stephen_Bennett.mp3")
BGM.set_volume(0.5)
BGM.play(loops=-1)


# Images
BG = pygame.image.load("Backgrounds/background.png").convert_alpha()
BG = pygame.transform.scale(BG, (1280, 720))

# Swordsman Animations
# IDLE
swordsman_idle_sheet_image = pygame.image.load('Swordsman/Idle.png').convert_alpha()
swordsman_idle_sheet = spritesheet.SpriteSheet(swordsman_idle_sheet_image)
# ATTACK 01
swordsman_attack1_sheet_image = pygame.image.load("Swordsman/Attack_1.png").convert_alpha()
swordsman_attack1_sheet = spritesheet.SpriteSheet(swordsman_attack1_sheet_image)
# HURT
swordsman_hurt_sheet_image = pygame.image.load('Swordsman/Hurt.png').convert_alpha()
swordsman_hurt_sheet = spritesheet.SpriteSheet(swordsman_hurt_sheet_image)
# DEAD
swordsman_dead_sheet_image = pygame.image.load("Swordsman/Dead.png").convert_alpha()
swordsman_dead_sheet = spritesheet.SpriteSheet(swordsman_dead_sheet_image)
# WALK
swordsman_walk_sheet_image = pygame.image.load("Swordsman/Pick_Up.png").convert_alpha()
swordsman_walk_sheet = spritesheet.SpriteSheet(swordsman_walk_sheet_image)

# Build Animations
animation_frames = [] # 0: Idle, 1: Attack1, 2: Hurt, 3: Dead, 4: Walk
temp_list = []
# IDLE
for i in range(5):
    temp_list.append(swordsman_idle_sheet.get_image(i, 128, 128, 2, BLACK))
animation_frames.append(temp_list)
temp_list = []
# ATTACK1
for i in range(4):
    temp_list.append(swordsman_attack1_sheet.get_image(i, 128, 128, 2, BLACK))
animation_frames.append(temp_list)
temp_list = []
# HURT
for i in range(3):
    temp_list.append(swordsman_hurt_sheet.get_image(i, 128, 128, 2, BLACK))
animation_frames.append(temp_list)
temp_list = []
# DEAD
for i in range(4):
    temp_list.append(swordsman_dead_sheet.get_image(i, 128, 128, 2, BLACK))
animation_frames.append(temp_list)
temp_list = []
# WALK
for i in range(8):
    temp_list.append(swordsman_walk_sheet.get_image(i, 128, 128, 2, BLACK))
animation_frames.append(temp_list)
# temp_list = []
# Call player
swordsman = fighter.Fighter(animation_frames, 0, 310, 525)

run = True
while run:
    # Background and FPS
    CLOCK.tick(FPS)
    SCREEN.blit(BG, (0, 0))

    # EVENT handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        # Keyboard input
        if event.type == pygame.KEYDOWN:
            # ATTACK1
            if event.key == pygame.K_SPACE:
                swordsman.frame_index = 0
                swordsman.action = 1
            # MOVEMENT
            # Right
            if event.key == pygame.K_d:
                swordsman.frame_index = 0
                swordsman.action = 4
                swordsman.move_right = True
                swordsman.flip_h = False
            # Left
            if event.key == pygame.K_a:
                swordsman.frame_index = 0
                swordsman.action = 4
                swordsman.move_left = True
                swordsman.flip_h = True
            # Run
            if event.key == pygame.K_LSHIFT:
                swordsman.run = True
        if event.type == pygame.KEYUP:
            # ATTACK1
            # if event.key == pygame.K_SPACE:
            #     swordsman.frame_index = 0
            #     swordsman.action = 0
            # Right
            if event.key == pygame.K_d:
                swordsman.frame_index = 0
                swordsman.action = 0
                swordsman.move_right = False
            # Left
            if event.key == pygame.K_a:
                swordsman.frame_index = 0
                swordsman.action = 0
                swordsman.move_left = False
            # Run
            if event.key == pygame.K_LSHIFT:
                swordsman.run = False

    # Draw swordsman
    swordsman.update(SCREEN)


    pygame.display.update()

pygame.quit()
