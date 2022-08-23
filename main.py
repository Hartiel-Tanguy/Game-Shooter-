import pygame
import math
pygame.init()
from game import Game
from player import Player


#definir une clock (fps)
clock = pygame.time.Clock()
FPS = 200

#generé la fenetre du jeux 

pygame.display.set_caption("game shooter")
screen = pygame.display.set_mode((1080,720))

#importé de chargé l'arriere plant de notre jeux 
background = pygame.image.load('assets/bg.jpg')

#chargé la banièree de demarage du jeux
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#importé le bouton de demarage du jeux
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

#charger notre jeux
game = Game()


#chargé le joueur

running = True
#boucle tanr que cette condision est maintenue vrai
while running:

    #applique l'arriere plan 
    screen.blit(background, (0,-200))

    #vdeclenchez le jeux si commencé
    if game.is_playing:
        game.update(screen)
    #verifier si le jeux a commencé 
    else :  
        #ajouté le bouton de demarage du jeux
        screen.blit(play_button, play_button_rect)
        #ajouté mon ecran de demarage du jeux
        screen.blit(banner, banner_rect)
   
    #metre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre alors la condition est false
    for event in pygame.event.get():
        #si la condition est false alors la boucle est interrompue
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #detecté si le joueur appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecté si le joueur relache une touche pour le projectile
            if event.key == pygame.K_SPACE:
                game.player.Launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si le joueur a cliqué sur le bouton de demarage du jeux
            if play_button_rect.collidepoint(event.pos):
                #metre le jeux en cours
                game.start()
    #fixé le nombre de fps
    clock.tick(FPS)