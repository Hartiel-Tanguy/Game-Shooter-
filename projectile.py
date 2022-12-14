import pygame


#definir la calss projectile

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x +140
        self.rect.y = player.rect.y +70
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourné le projectile
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)


    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #si le projectile entre en collision avec un monstre alors le projectile est supprimé
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

        #verifier si le projectile est sortie de l'ecran
        if self.rect.x > 1080:
            self.remove()
