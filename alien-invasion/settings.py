class Settings:
    """所有设置用此类管理"""
    
    def __init__(self):
        #默认窗口设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #全屏模式
        self.full_screen = True
        
        #ship设置
        self.ship_speed = 1