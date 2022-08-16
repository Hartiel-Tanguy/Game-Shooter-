import pygame
from player import Player


#class qui représente le jeux 
class Game:

    def __init__(self):
        #generer le joeur
        self.player = Player()
        self.pressed = {}
    
