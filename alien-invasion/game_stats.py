
class GameStats:
    #记录统计信息
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score = 0
        
    def reset_stats(self):
        self.game_active = False
        self.ship_life = self.settings.ship_life
        self.score = 0
        self.level = 1