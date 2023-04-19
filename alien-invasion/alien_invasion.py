import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init() #初始化pygame实例
        self.screen = pygame.display.set_mode((1200, 800)) #创建窗口，本质是构建surface对象，并赋值给类的screen
        pygame.display.set_caption("Alien Invasion") #设置标题
        
    def run_game(self): #枚举的event检测去对surface对象刷新重绘或退出
        while True: #持续监听事件并处理
            for event in pygame.event.get(): #获取从上次get()到本次get()之间发生的所有事件，事件包括用户的按键，鼠标等操作
                if event.type == pygame.QUIT:
                    sys.exit()
            
            pygame.display.flip() #刷新窗口：重绘surface并覆盖旧的surface

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()