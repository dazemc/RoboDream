import pygame

walk_sfx_file = 'Characters/Swordsman/SFX/Pick_UP.wav'
attack_1_sfx_file = 'Characters/Swordsman/SFX/Attack_1.wav'

skeleton_walk_sfx_file = 'Characters/Skeleton_Warrior/SFX/skeleton_step.mp3'
skeleton_attack_sfx_file = 'Characters/Skeleton_Warrior/SFX/skeleton_attack.mp3'

class Fighter:
    def __init__(self, animation_frames, action, x, y):
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_frames = animation_frames
        self.action = action
        self.x = x
        self.y = y
        self.run = False
        self.move_right = False
        self.move_left = False
        self.flip_h = False
        self.move = True
        self.alive = True
        self.enemy = False
        self.stop_animation = False
        self.first_start = True


    def main_update(self, screen):

        # ANIMATION
        animation_cooldown = 100  # ms
        image = self.animation_frames[self.action][self.frame_index]
        self.rect = image.get_rect()
        # MASK for collision
        self.mask = pygame.mask.from_surface(image)
        mask_image = self.mask.to_surface()
        mask_image.set_colorkey((0, 0, 0))
        self.rect.center = (self.x, self.y)


        # MOVEMENT/SFX
        if self.alive:
            if self.action == 4:
                if self.run:
                    move_increments = 10
                else:
                    move_increments = 5
                if self.move_right:
                    self.x += move_increments
                    if self.frame_index % 2 == 0:
                        walk_sfx = pygame.mixer.Sound(walk_sfx_file)
                        walk_sfx.set_volume(0.3)
                        walk_sfx.play(maxtime=600)
                if self.move_left:
                    self.x -= move_increments
                    if self.frame_index % 2 == 0:
                        walk_sfx = pygame.mixer.Sound(walk_sfx_file)
                        walk_sfx.set_volume(0.3)
                        walk_sfx.play(maxtime=600)
                if self.x >= 1280 + 128:
                    self.x = 0
                if self.x < -128:
                    self.x = 1280

            # SFX
            if self.action == 1:
                attack_1_sfx = pygame.mixer.Sound(attack_1_sfx_file)
                attack_1_sfx.set_volume(0.5)
                attack_1_sfx.play(maxtime=800)

            if (pygame.time.get_ticks() - self.update_time) > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            # End of Animations
            if self.frame_index >= len(self.animation_frames[self.action]):
                # Stay dead
                # if self.action == 3:
                #     self.frame_index = len(self.animation_frames[self.action]) - 1
                if self.action == 1:

                    self.action = 0
                else:
                    self.frame_index = 0

        else:
            if not self.stop_animation:
                self.action = 3
                if (pygame.time.get_ticks() - self.update_time) > animation_cooldown:
                    self.update_time = pygame.time.get_ticks()
                    self.frame_index += 1
                # End of Animations
                if self.frame_index >= len(self.animation_frames[self.action]):
                    # Stay dead
                    if self.action == 3:
                        self.frame_index = len(self.animation_frames[self.action]) - 1
                        self.action = 3
                        self.stop_animation = True





        # Draw image
        if self.flip_h:
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey((0, 0, 0))
            self.mask = pygame.mask.from_surface(image)
            mask_image = self.mask.to_surface()
            mask_image.set_colorkey((0, 0, 0))
        screen.blit(image, self.rect)
        # screen.blit(mask_image, self.rect)


    def enemy_update(self, screen):

        # Declare as enemy
        self.enemy = True

        # ANIMATION
        animation_cooldown = 200  # ms
        image = self.animation_frames[self.action][self.frame_index]
        self.rect = image.get_rect()
        self.rect = self.rect.inflate(-200, -200)
        self.mask = pygame.mask.from_surface(image)
        mask_image = self.mask.to_surface()
        mask_image.set_colorkey((0, 0, 0))
        self.rect.center = (self.x, self.y)

        # MOVEMENT/SFX
        if self.x > -128:
            if self.alive:
                if self.action == 4:
                    if self.run:
                        move_increments = 6
                    else:
                        move_increments = 2
                    if self.move_right:
                        self.x += move_increments
                        if self.frame_index % 2 == 0:
                            walk_sfx = pygame.mixer.Sound(skeleton_walk_sfx_file)
                            walk_sfx.set_volume(0.3)
                            walk_sfx.play(maxtime=600)
                    if self.move_left:
                        self.x -= move_increments
                        if self.frame_index % 2 == 0:
                            walk_sfx = pygame.mixer.Sound(skeleton_walk_sfx_file)
                            walk_sfx.set_volume(0.3)
                            walk_sfx.play(maxtime=600)


                # SFX
                if self.action == 1:
                    attack_1_sfx = pygame.mixer.Sound(skeleton_attack_sfx_file)
                    attack_1_sfx.set_volume(0.5)
                    attack_1_sfx.play(maxtime=800)

                if (pygame.time.get_ticks() - self.update_time) > animation_cooldown:
                    self.update_time = pygame.time.get_ticks()
                    self.frame_index += 1
                # End of Animationsd
                if self.frame_index >= len(self.animation_frames[self.action]):
                    if self.action == 1:
                        self.frame_index = 0
                        self.action = 4
                    else:
                        self.frame_index = 0
                        self.action = 1
            else:
                if not self.stop_animation:
                    if (pygame.time.get_ticks() - self.update_time) > animation_cooldown:
                        self.update_time = pygame.time.get_ticks()
                        self.frame_index += 1
                    # End of Animations
                    if self.frame_index >= len(self.animation_frames[self.action]):
                        # Stay dead
                        if self.action == 3:
                            self.frame_index = len(self.animation_frames[self.action]) - 1
                            self.action = 3
                            self.stop_animation = True

                # Draw image
            if self.flip_h:
                image = pygame.transform.flip(image, True, False)
                image.set_colorkey((0, 0, 0))
                self.mask = pygame.mask.from_surface(image)
                mask_image = self.mask.to_surface()
                mask_image.set_colorkey((0, 0, 0))
            screen.blit(image, self.rect)
            # screen.blit(mask_image, self.rect)

        # Attacking player
        if self.move == True:
            self.x += 2

