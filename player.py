import pygame
from projectile import Projectile


#creations du joueur 
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 1.5
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_health_bar(self, surface):
        #dessiner l'arriere plan de la bar de vie
        pygame.draw.rect(surface, (60, 63, 60) , [self.rect.x +50, self.rect.y +20, self.max_health, 7])
        #dessiner la bar de vie 
        pygame.draw.rect(surface, (111, 210, 46) , [self.rect.x +50, self.rect.y + 20, self.health, 7])

    def Launch_projectile(self):
        #crée nouvelle instance de projectile
        self.all_projectiles.add(Projectile(self))
    def move_right(self):
        #deplacement que si le joueur n'est pas en collission avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity