import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init() #初始化pygame实例
        
        #初始化AlienInvasion的成员
        self.settings = Settings() #构造Settings类型的成员
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #构造screen成员，即游戏主屏幕
        
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self) #构造ship成员，传入参数是当前类，这样完成了两个类对象的互相关联
        
    def run_game(self): #枚举的event检测去对surface对象刷新重绘或退出
        while True: #持续监听事件并处理
            self._check_events() #注意python的self是显式的，所以在类内调用方法也必须用self去调用，这一点和C++的隐式this支持直接调用类内方法不同
            self.ship.update() #根据ship的移动状态更新ship位置
            self._update_screen() #注意self.的调用方式已经隐式地将self传参到_check_events(), _update_screen()，不需要再显式传入self
            
    # 类内部的helper function通常加前缀下划线命名
    # helper function只是为了将复杂的函数拆分重构，不是对外开放的方法，类似C++的static inline函数
    def _check_events(self):
        for event in pygame.event.get(): #获取从上次get()到本次get()之间发生的所有事件，事件包括用户的按键，鼠标等操作
            if event.type == pygame.QUIT: #退出按钮
                sys.exit()
            elif event.type == pygame.KEYDOWN: #有键盘按键按下
                if event.key == pygame.K_RIGHT: #具体的键是方向右键
                    self.ship.moving_right = True #这里只设置状态，而不直接设置坐标
                if event.key == pygame.K_LEFT: 
                    self.ship.moving_left = True 
            elif event.type == pygame.KEYUP: #松开键盘按键
                if event.key == pygame.K_RIGHT: #具体的键是方向右键
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT: 
                    self.ship.moving_left = False 
                    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) #填充颜色到surface类型的screen对象
        self.ship.blitme() #绘制ship
        pygame.display.flip() #刷新窗口：重绘所有surface并覆盖旧的surface
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()