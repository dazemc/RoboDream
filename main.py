import pygame
import spritesheet, fighter
from pygame.locals import *

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

# Stores animations into a list so they can be accessed by their index
# 0: Idle, 1: Attack1, 2: Hurt, 3: Dead, 4: Walk
def build_animations(frame_number, spritesheet, xy, scale, color_key):
    animation_list = []
    for i in range(frame_number):
        animation_list.append(spritesheet.get_image(i, xy, xy, scale, color_key))
    return animation_list

# Swordsman Animations
# IDLE
swordsman_idle_sheet_image = pygame.image.load('Characters/Swordsman/Idle.png').convert_alpha()
swordsman_idle_sheet = spritesheet.SpriteSheet(swordsman_idle_sheet_image)
# ATTACK 01
swordsman_attack1_sheet_image = pygame.image.load("Characters/Swordsman/Attack_1.png").convert_alpha()
swordsman_attack1_sheet = spritesheet.SpriteSheet(swordsman_attack1_sheet_image)
# HURT
swordsman_hurt_sheet_image = pygame.image.load('Characters/Swordsman/Hurt.png').convert_alpha()
swordsman_hurt_sheet = spritesheet.SpriteSheet(swordsman_hurt_sheet_image)
# DEAD
swordsman_dead_sheet_image = pygame.image.load("Characters/Swordsman/Dead.png").convert_alpha()
swordsman_dead_sheet = spritesheet.SpriteSheet(swordsman_dead_sheet_image)
# WALK
swordsman_walk_sheet_image = pygame.image.load("Characters/Swordsman/Pick_Up.png").convert_alpha()
swordsman_walk_sheet = spritesheet.SpriteSheet(swordsman_walk_sheet_image)

# Skeleton Animations
# IDLE
skeleton_idle_sheet_image = pygame.image.load('Characters/Skeleton_Warrior/Idle.png').convert_alpha()
skeleton_idle_sheet = spritesheet.SpriteSheet(skeleton_idle_sheet_image)
# ATTACK3
skeleton_attack1_sheet_image = pygame.image.load('Characters/Skeleton_Warrior/Attack_3.png').convert_alpha()
skeleton_attack1_sheet = spritesheet.SpriteSheet(skeleton_attack1_sheet_image)
# HURT
skeleton_hurt_sheet_image = pygame.image.load('Characters/Skeleton_Warrior/Hurt.png').convert_alpha()
skeleton_hurt_sheet = spritesheet.SpriteSheet(skeleton_hurt_sheet_image)
# DEAD
skeleton_dead_sheet_image = pygame.image.load('Characters/Skeleton_Warrior/Dead.png').convert_alpha()
skeleton_dead_sheet = spritesheet.SpriteSheet(skeleton_dead_sheet_image)
# Walk
skeleton_walk_sheet_image = pygame.image.load('Characters/Skeleton_Warrior/Walk.png').convert_alpha()
skeleton_walk_sheet = spritesheet.SpriteSheet(skeleton_walk_sheet_image)
# Build Animations for Swordsman
swordsman_animation_frames = []
temp_list = []
# IDLE
swordsman_animation_frames.append(build_animations(5, swordsman_idle_sheet, 128, 2, BLACK))
# ATTACK1
swordsman_animation_frames.append(build_animations(4, swordsman_attack1_sheet, 128, 2, BLACK))
# HURT
swordsman_animation_frames.append(build_animations(3, swordsman_hurt_sheet, 128, 2, BLACK))
# DEAD
swordsman_animation_frames.append(build_animations(4, swordsman_dead_sheet, 128, 2, BLACK))
# WALK
swordsman_animation_frames.append(build_animations(8, swordsman_walk_sheet, 128, 2, BLACK))
# temp_list = []
# Call player
swordsman = fighter.Fighter(swordsman_animation_frames, 0, 600, 525)

# Skeleton Animation
skeleton_animation_frames = []
# IDLE
skeleton_animation_frames.append(build_animations(7, skeleton_idle_sheet, 128, 2, BLACK))
# ATTACK3
skeleton_animation_frames.append(build_animations(4, skeleton_attack1_sheet, 128, 2, BLACK))
# Hurt
skeleton_animation_frames.append(build_animations(2, skeleton_hurt_sheet, 128, 2, BLACK))
# DEAD
skeleton_animation_frames.append(build_animations(4, skeleton_dead_sheet, 128, 2, BLACK))
#WALK
skeleton_animation_frames.append(build_animations(7, skeleton_walk_sheet, 128, 2, BLACK))
# Call enemies
# Skeleton
if swordsman.first_start:
    skeleton1 = fighter.Fighter(skeleton_animation_frames, 4, 100, 430)

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
    swordsman.main_update(SCREEN)
    skeleton1.enemy_update(SCREEN)

    # Collision
    # if swordsman.action == 1:
    #     swordsman.rect.inflate(300, 300)
    #     if swordsman.rect.colliderect(skeleton1.rect):
    #         if skeleton1.alive == False:
    #             print("Not Dead")
    #         if skeleton1.alive:
    #             print("Dead")
    #         if swordsman.action == 1:
    #             skeleton1.frame_index = 0
    #             skeleton1.action = 3
    #             skeleton1.move = False
    #             skeleton1.alive = False

    if swordsman.mask.overlap(skeleton1.mask, (skeleton1.rect.x - swordsman.rect.x, skeleton1.rect.y - swordsman.rect.y)):
        if swordsman.action == 1:
            skeleton1.action = 3
            skeleton1.move = False
            if skeleton1.alive:
                skeleton1.frame_index = 0
                skeleton1.alive = False
        if skeleton1.action == 1:
            if swordsman.alive:
                swordsman.frame_index = 0
                swordsman.alive = False
        if not swordsman.alive:
            pygame.event.set_blocked(KEYDOWN)
            pygame.event.set_blocked(KEYUP)

    pygame.display.update()

pygame.quit()
