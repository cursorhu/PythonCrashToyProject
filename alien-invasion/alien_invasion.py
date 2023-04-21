import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init() #初始化pygame实例
        
        #初始化AlienInvasion的成员
        self.settings = Settings() #构造Settings类型的成员
        self._set_screen() #设置游戏窗口
        
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self) #构造ship成员，传入参数是当前类，这样完成了两个类对象的互相关联
        
        self.bullets = pygame.sprite.Group() #创建编组，用于管理bullet
        
        
    def run_game(self): #枚举的event检测去对surface对象刷新重绘或退出
        while True: #持续监听事件并处理
            self._check_events() #注意python的self是显式的，所以在类内调用方法也必须用self去调用，这一点和C++的隐式this支持直接调用类内方法不同
            self.ship.update() #根据ship的移动状态更新ship位置
            self.bullets.update() #更新所有bullet的位置; 对sprite.Group编组调用某方法，实际效果是对组内的每个Sprite对象调用该方法, Bullet ‘is-a’ Sprite对象，最终调用Bullet的update方法
            self._update_screen() #绘制屏幕的所有元素; 注意self.func()的调用方式隐式地将self作为参数传到func()
            
    # 类内部的helper function通常加前缀下划线命名
    # helper function只是为了将复杂的函数拆分重构，不是对外开放的方法，类似C++的static inline函数
    def _check_events(self):
        for event in pygame.event.get(): #获取从上次get()到本次get()之间发生的所有事件，事件包括用户的按键，鼠标等操作
            if event.type == pygame.QUIT: #退出按钮
                sys.exit()
            elif event.type == pygame.KEYDOWN: #有键盘按键按下
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: #松开键盘按键
                self._check_keyup_events(event)
    
    def _set_screen(self):
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #窗口设置为从屏幕左上角到全屏右下角
            #self.screen.screen_width = self.screen.get_rect().width
            #self.screen.screen_height = self.screen.get_rect().height
        else: 
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #窗口设置为指定大小
               
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) #填充颜色到surface类型的screen对象
        self.ship.blitme() #绘制ship
        for bullet in self.bullets.sprites(): #sprites方法返回列表，包含调用者group的所有bullet对象
            bullet.draw_bullet() #调用bullet实现的绘制方法
        pygame.display.flip() #刷新窗口：重绘所有surface并覆盖旧的surface
     
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT: #具体的键是方向右键
            self.ship.moving_right = True #这里只设置状态，而不直接设置坐标
        if event.key == pygame.K_LEFT: 
            self.ship.moving_left = True
        if event.key == pygame.K_q: #q键退出，用于全屏模式
            sys.exit()
        if event.key == pygame.K_SPACE: 
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT: #具体的键是方向右键
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT: 
            self.ship.moving_left = False 
            
    def _fire_bullet(self):
        new_bullet = Bullet(self) #创建bullet实例
        self.bullets.add(new_bullet) #加入group    
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()