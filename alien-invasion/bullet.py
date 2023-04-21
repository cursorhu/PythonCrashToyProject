import pygame
from pygame.sprite import Sprite #sprite类能将游戏元素编组(Group)，方便操作组中所有元素

class Bullet(Sprite): #类的参数表示继承，Bullet继承Sprite类
    def __init__(self, ai_game):
        #创建bullet对象，初始化父类和子类成员
        super().__init__() #初始化父类的实例，目的是能让子类调用父类的方法
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #创建bullet的rect，并设置坐标和ship对齐 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #bullet的纵坐标位置
        self.y = float(self.rect.y)
        
    def update(self):
        self.y -= self.settings.bullet_speed #向上移动
        self.rect.y = self.y #更新位置
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect) #绘制bullet
            