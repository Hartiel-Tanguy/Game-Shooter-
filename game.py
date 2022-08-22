import pygame
from player import Player
from monster import Monster


#class qui représente le jeux 
class Game:

    def __init__(self,):
        #definir si notre jeux est en cours ou pas
        self.is_playing = False
        #generer le joeur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        #verifier si le joueur vas gauche ou droite
        if self.pressed.get(pygame.K_RIGHT)and self.player.rect.x < 914:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -33:
            self.player.move_left()
        
        print(self.player.rect.x)

        #applique le joueur
        screen.blit(self.player.image, self.player.rect)

        #applique la bar de vie
        self.player.update_health_bar(screen)

        #récupéré les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        #move des monstre
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        #applique l'image des projectiles
        self.player.all_projectiles.draw(screen)

        #applique le groupe de monstre
        self.all_monsters.draw(screen)


    def spawn_monster(self):
        self.all_monsters.add(Monster(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
