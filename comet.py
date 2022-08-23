import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,2)
        self.rect.x = random.randint(20, 800)
        self.rect.y = -random.randint(0, 500)
        self.comet_event = comet_event
        

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #verifié  qu'il nny ai plus de comete
        if len(self.comet_event.all_comets) == 0:
            print("pas de comete")
            #remetre la barre a 0
            self.comet_event.reset_percent()
            #réaparaitre les monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

        
    def fall(self):
        self.rect.y += self.velocity

        #elle tombe pas sur le sol 
        if self.rect.y > 550:
            print("sol")
        #retiré la boule de feux
            self.remove()

            #si si n'y a plus de boule de feux sur le jeux 
            if len(self.comet_event.all_comets) ==0 :
                #remetre le jeux en état initial
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #verifier si la boule de feux est en collision avec le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players):
            print("collision")
            self.remove()
            self.comet_event.game.player.damage(20)

        

    