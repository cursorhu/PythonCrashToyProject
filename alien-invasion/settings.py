class Settings:
    """所有设置用此类管理"""
    
    def __init__(self):
        self._init_static_setting()
        self.init_play_settings()
        
    def _init_static_setting(self):
        """Initialize settings that is static."""
        #默认窗口设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #全屏模式
        self.full_screen = False
        
        #ship设置
        #self.ship_speed = 1
        self.ship_life = 3
        
        #bullet设置
        #self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
        
        #alien设置
        #self.alien_speed = 1.0 #水平移动速度
        self.fleet_drop_speed = 10 #撞到边缘向下移动
        self.fleet_direction = 1 #1:右移，-1：左移
        
        #升级的配置
        self.speedup_scale = 1.1 #整体游戏速率提高
        self.score_scale = 1.5 #得分提高比率
        
    def init_play_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.alien_points = 50 # Scoring

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)