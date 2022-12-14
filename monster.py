import pygame
import random
import animation
class Monster(animation.AnimateSrpite):
    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1,3)

    def damage(self, amount):
        self.health -= amount

        #verifier si le monstre est mort
        if self.health <= 0:            
            #faire réapparaitre le monstre detruit 
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health


            #si la barre d'event comet est active
            if self.game.comet_event.is_full_loaded():
                #retitre le monstre
                self.game.all_monsters.remove(self)
                #appele de la methode pour verifier si la barre est chargé
                self.game.comet_event.attempt_fall()


    def update_animation(self):
        self.animate()

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
        #si le monstre est en collisiont avec le joueur
        else:
            #infligé des dégats au joueur
            self.game.player.damage(self.attack)



