import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 1

    def update_health_bar(self, surface):
        #definir une couleur pour la jauge de vie (RGB)
        bar_color = (255,0,0)
        #definir l'arriere plant de la jauge de vie
        back_color = (60, 63, 30)


        #definir la posision de la jeuge de vie 
        bar_position = [self.rect.x + 10, self.rect.y- 20 ,self.health , 5]
        #definir la position de l'arriere plan de la jauge de vie
        back_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        #dessiner l'arriere plan de la bar de vie
        pygame.draw.rect(surface, back_color, back_position)
        #dessiner la bar de vie 
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        #deplacement ne se fais que ssi pas de collision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity


