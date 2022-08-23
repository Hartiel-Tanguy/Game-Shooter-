import pygame
import math

#definir une class d'animation
class AnimateSrpite(pygame.sprite.Sprite):

    #definir es chose a faire lors de l'animation
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.images = animation.get('sprite_name')
    #animé le sprites
    # def animate(self):
    #     self.current_image += 1
    #     if self.current_image >= len (self.images):
    #         self.current_image = 0
    #     self.image = self.images[self.current_image]
     
#definir une fonction pour chargé les image de l'animation
def load_animation_images(sprite_name):
    #charger les image dans le dossié assets
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucle pour chaque image dans le dossié 
    for num in range (1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    #renvoyé le contenue de la liste
    return images


#definir un dictionnaire qui vas contenir les image de tout les sprites
animation = {
    "mummy": load_animation_images("mummy")
}
