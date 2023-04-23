from time import sleep
import pygame.font

class Button:
    def __init__(self, ai_game, msg): #msg: button中显示的文本
        self.screen = ai_game.screen
        #设置button属性
        self.width, self.height = 200, 50
        self.btn_color = (0, 255, 0)
        self.txt_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #使用默认字体
        #创建对象(rect)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen.get_rect().center
        #创建字体内容
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        #渲染，将文本转换为图像，参数为：
        #文本，反锯齿，文本颜色，背景色
        self.msg_img =self.font.render(msg, True, self.txt_color, self.btn_color) 
        self.msg_rect = self.msg_img.get_rect()
        self.msg_rect.center = self.rect.center
        
    def draw_button(self):
        #先绘制button,再绘制msg
        self.screen.fill(self.btn_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_rect)