from typing_extensions import Self
import pygame

#definir une class d'animation
class AnimateSrpite(pygame.sprite.Sprite):

    #definir es chose a faire lors de l'animation
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load('assets/' + sprite_name + '.png')
