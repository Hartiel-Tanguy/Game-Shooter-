import pygame
from projectile import Projectile


#creations du joueur 
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def Launch_projectile(self):
        #crée nouvelle instance de projectile
        self.all_projectiles.add(Projectile(self))
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity