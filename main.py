import pygame
pygame.init()
from game import Game
from player import Player
#generé la fenetre du jeux 

pygame.display.set_caption("game shooter")
screen = pygame.display.set_mode((1080,720))

#importé de chargé l'arriere plant de notre jeux 
background = pygame.image.load('assets/bg.jpg')


#charger notre jeux
game = Game()


#chargé le joueur

player = Player()

running = True
#boucle tanr que cette condision est maintenue vrai
while running:

    #applique l'arriere plan 
    screen.blit(background, (0,-200))

    #verifier si le joueur vas gauche ou droite
    if game.pressed.get(pygame.K_RIGHT)and game.player.rect.x < 914:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -33:
        game.player.move_left()
    
    print(game.player.rect.x)

    #applique le joueur
    screen.blit(game.player.image, game.player.rect)

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
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False