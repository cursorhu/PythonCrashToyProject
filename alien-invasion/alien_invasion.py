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
            for event in pygame.event.get(): #获取从上次get()到本次get()之间发生的所有事件，事件包括用户的按键，鼠标等操作
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color) #填充颜色到surface类型的screen对象
            self.ship.blitme() #绘制ship
            
            pygame.display.flip() #刷新窗口：重绘所有surface并覆盖旧的surface

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()