import pygame
#pygame能以矩形对象处理游戏中的图像元素，矩形大小和坐标可以表达该图像元素在整个屏幕中的位置
#矩形坐标可以方便地实现碰撞检测
class Ship:
    def __init__(self, ai_game):
        #将外部类的对象赋值给当前类的成员，目的是使当前类可以使用外部类的所有方法(本例为blit方法)
        #python的任意类成员的初始化都是直接赋值而不需要声明也不考虑类型；
        #下面的类实例赋值语句可以近似理解为自动实现了类似C++的拷贝构造
        self.screen = ai_game.screen #Ship screen定义为game screen
        self.screen_rect = ai_game.screen.get_rect() #Ship screen的矩形区域定义为和game screen矩形区域相同的坐标
        
        #加载图像，获取其边界矩形坐标
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #将图像和屏幕区域对齐，使图像位于屏幕底部正中间
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        #指定位置绘制图像
        self.screen.blit(self.image, self.rect)