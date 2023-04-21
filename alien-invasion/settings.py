class Settings:
    """所有设置用此类管理"""
    
    def __init__(self):
        #默认窗口设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #全屏模式
        self.full_screen = False
        
        #ship设置
        self.ship_speed = 1
        
        #bullet设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        
        self.bullet_allowed = 5