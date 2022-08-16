import pygame
pygame.init()

#generé la fenetre du jeux 

pygame.display.set_caption("game shooter")
screen = pygame.display.set_mode((1080,720))

#importé de chargé l'arriere plant de notre jeux 
background = pygame.image.load('assets/bg.jpg')

running = True
#boucle tanr que cette condision est maintenue vrai
while running:

    #applique l'arriere plan 
    screen.blit(background, (0,-200))

    #metre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre alors la condition est false
    for event in pygame.event.get():
        #si la condition est false alors la boucle est interrompue
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()