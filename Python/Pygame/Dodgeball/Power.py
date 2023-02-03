from settings import *
from functions import *
import random

class Power(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((si.current_h/35,si.current_h/35))
        self.rect = pygame.draw.rect(self.image, "#FFFF00" ,self.image.get_rect())
        self.cw = int(self.rect.w/2)
        self.rect.center = (random.randint(self.cw,P_WIDTH - self.cw),random.randint(self.cw,P_WIDTH - self.cw))
        self.time = 7
    def respawn(self):
        self.rect.center = (random.randint(self.cw,P_WIDTH - self.cw),random.randint(self.cw,P_WIDTH - self.cw))

    def update(self):
        PLAY.blit(self.image,self.rect)