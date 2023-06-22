import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), area=((frame * width), 0, width, height))
        image = pygame.transform.rotozoom(image, 0, scale)
        image.set_colorkey(color)
        return image
