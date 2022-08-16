import pygame
pygame.init()

#creations du joueur 
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()

#generé la fenetre du jeux 

pygame.display.set_caption("game shooter")
screen = pygame.display.set_mode((1080,720))

#importé de chargé l'arriere plant de notre jeux 
background = pygame.image.load('assets/bg.jpg')



#chargé le joueur

player = Player()

running = True
#boucle tanr que cette condision est maintenue vrai
while running:

    #applique l'arriere plan 
    screen.blit(background, (0,-200))


    #applique le joueur
    screen.blit(player.image, player.rect)

    #metre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre alors la condition est false
    for event in pygame.event.get():
        #si la condition est false alors la boucle est interrompue
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()