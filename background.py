import pygame

class Background(pygame.sprite.Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load('images/back.png')
        self.rect = self.image.get_rect()

