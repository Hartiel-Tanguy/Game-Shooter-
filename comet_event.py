from ast import Is
import pygame
from comet import Comet


#crée une classe pour geré l'event
class CometFallEvent:

    #lors du charchement crée un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        #definir un grope de comet 
        self.all_comets = pygame.sprite.Group()

    def add_percent(self,):
        self.percent += self.percent_speed/70

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #apparaitre des comets
        for i in range(0, 10):
            self.all_comets.add(Comet(self))

        
    def attempt_fall(self):
        #la jauge est totaaement chargé??
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluit de comete")
            self.meteor_fall()
            self.fall_mode = True


    def update_bar(self, surface):

        #ajout" du pourcentage de la barre d'event
        self.add_percent()

        #barre noir en arrière plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #axe des x
            surface.get_height() - 20, #axe des y
            surface.get_width(), #longeur de la fenêtre
            10 #epaiseur de la barre
        ])
        #la barre rouoge j'auge d'event
        pygame.draw.rect(surface, (187, 11, 11), [
            0, #axe des x
            surface.get_height() - 20, #axe des y
            (surface.get_width() /100) * self.percent , #longeur de la fenêtre
            10 #epaiseur de la barre
        ])
