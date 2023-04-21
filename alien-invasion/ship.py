import pygame
#pygame能以矩形对象处理游戏中的图像元素，矩形大小和坐标可以表达该图像元素在整个屏幕中的位置
#矩形坐标的值是以坐上角为原点：窗口左上角为(0,0)，右下角为最大值(1200,800)，和QT/MFC的GUI框架一样
#用矩形表示任意形状的对象，可以方便地实现碰撞检测，边界检测等
class Ship:
    def __init__(self, ai_game):
        #将外部类的对象赋值给当前类的成员，目的是使当前类可以使用外部类的所有方法(本例为blit方法)
        #python的任意类成员的初始化都是直接赋值而不需要声明也不考虑类型；
        #类实例的赋值语句可以近似理解为自动实现了类似C++的拷贝构造
        self.screen = ai_game.screen #Ship screen定义为game screen
        self.screen_rect = ai_game.screen.get_rect() #Ship screen的矩形区域定义为和game screen矩形区域相同的坐标
        self.settings = ai_game.settings #使用game setting的成员
        
        #加载图像，获取其边界矩形坐标
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #将图像和屏幕区域对齐，使图像位于屏幕底部正中间
        self.rect.midbottom = self.screen_rect.midbottom
        
        #支持小数倍速的移动：由于rect对象的x为整数，因此创建float x成员去支持小数坐标
        self.x = float(self.rect.x)
        
        #表示右移状态，使用此状态机可以支持持续按键移动
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        #指定位置绘制图像
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        #根据右移状态调整ship位置
        if self.moving_right and self.rect.right < self.screen_rect.right: #边界检测
            self.x += self.settings.ship_speed #支持小数倍速的坐标移动
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #float的整数部分赋值给rect坐标. 由于按键按下会持续一段时间因此有倍速移动的效果
        self.rect.x = self.x 