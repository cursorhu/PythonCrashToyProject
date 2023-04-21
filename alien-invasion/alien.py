import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #初始位置为左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #控制水平速度
        self.x = float(self.rect.x)
        
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction #方向正负*移动速度
        self.rect.x = self.x
        
    def check_edge(self):
        screen_rect = self.screen.get_rect() #screen范围
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: #边缘检测
            return True