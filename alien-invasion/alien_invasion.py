import sys
import pygame

from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):
        pygame.init() #初始化pygame实例
        
        #初始化成员
        self.settings = Settings() #构造Settings类型的成员
        self._set_screen() #设置游戏窗口
        pygame.display.set_caption("Alien Invasion")
        
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        
        self.ship = Ship(self) #构造ship成员；传入参数是当前类是为了完成两个类互相关联，可调用对方类的方法
        self.aliens = pygame.sprite.Group() #创建一组alien，sprite.Group等同于python自带的列表数组类，支持碰撞检测等游戏专用方法
        self._create_fleet() 
        self.bullets = pygame.sprite.Group() #创建一组bullet，_fire_bullet创建具体实例
        
        self.play_button = Button(self, "Play")
        
        
    def run_game(self): #枚举的event检测去对surface对象刷新重绘或退出
        while True: #持续监听事件并处理
            self._check_events() #注意python的self是显式的，所以在类内调用方法也必须用self去调用，这一点和C++的隐式this支持直接调用类内方法不同
            if self.stats.game_active: #仅active状态才更新内容
                self.ship.update() #根据ship的移动状态更新ship位置
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN: #鼠标按下
                pos = pygame.mouse.get_pos()
                self._check_mouse_events(pos)
    
    def _set_screen(self):
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #窗口设置为从屏幕左上角到全屏右下角
        else: 
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #窗口设置为指定大小
               
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) #填充颜色到surface类型的screen对象
        self.ship.blitme() #绘制ship
        for bullet in self.bullets.sprites(): #sprites方法返回列表，包含调用者group的所有bullet对象
            bullet.draw_bullet() #调用bullet实现的绘制方法
        self.aliens.draw(self.screen) #绘制alien group的每一个alien到screen上
        self.scoreboard.show_score()
        
        if not self.stats.game_active: #最后绘制最上层的Play button
            self.play_button.draw_button()
        
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
    
    def _check_mouse_events(self, pos):
        #点击Play：鼠标点击坐标和button区域有重合
        clickplay = self.play_button.rect.collidepoint(pos)
        if clickplay and not self.stats.game_active: 
            self.stats.reset_stats()
            self._reset_battle()
            self.settings.init_play_settings()
            self.scoreboard.prep_score() #show score/level/shiplife
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships() 
            self.stats.game_active = True #enable game
            pygame.mouse.set_visible(False) #hide mouse when game is active      
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self) #创建bullet实例
            self.bullets.add(new_bullet) #加入group    
    
    def _update_bullets(self):
        #更新所有bullet的位置;
        self.bullets.update() #对sprite.Group编组调用某方法，实际效果是对组内的每个Sprite对象调用该方法, Bullet ‘is-a’ Sprite对象，最终调用Bullet的update方法    
        for bullet in self.bullets.copy(): #不能在遍历的时候删除成员，所有copy列表来遍历，删除原列表的成员
            if bullet.rect.bottom <= 0: #bullet底端超出game screen(纵坐标0)
                self.bullets.remove(bullet) #从列表中删除该成员
        #print(len(self.bullets)) #debug打印bullet个数：列表的长度即成员个数

        #检测bullet和alien是否碰撞
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        #sprite.groupcollide将两个group的每个元素比较是否有位置碰撞，返回一个包含多个key-value的map字典，表示所有碰撞对象
        #参数1为key, 参数2为value, 参数3，4为True表示碰撞后删除参数1或者2的对象
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions: #key-value类型
            self._update_score(collisions)

        #当所有Alien都被摧毁，升级到下一关
        if not self.aliens:
            self._update_level()
            
    def _update_level(self):
        # Increase game level and speed.
        self.stats.level += 1
        self.scoreboard.prep_level()
        self.settings.increase_speed()
        # Reset battle for next game level.
        self._reset_battle()        
    
    def _update_score(self, collisions):
        for aliens in collisions.values():
            self.stats.score += self.settings.alien_points * len(aliens)
        self.scoreboard.prep_score()
        self.scoreboard.check_high_score()
    
    def _update_aliens(self):
        self._check_fleet_edge() #更新整个group位置
        self.aliens.update() #对group中的每个alien对象调用其update()
        #检测alien和ship是否碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._alien_hit_ship()
        #检测alien是否到达底部
        self._alien_reach_bottom()
        
    def _create_fleet(self):
        alien = Alien(self) #只是为了计算边界和个数，不放入group
        alien_width, alien_height = alien.rect.size #size是元祖，包含横纵长度
        #计算一行能放多少个alien
        available_space_x = self.settings.screen_width - (2 * alien_width) #左右各预留一个alien宽度
        number_alien_x = available_space_x // (2 * alien_width) #各alien直接间隔一个alien宽度， //是整除，丢弃余数
        #计算一列能放多少个alien
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height #alien和ship距离多预留一点
        number_alien_y = available_space_y // (2 * alien_height)
        
        for row_index in range(number_alien_y):
            for alien_index in range(number_alien_x):
                self._create_alien(alien_index, row_index)
    
    def _create_alien(self, alien_index, row_index):
        alien = Alien(self) #要加入group的alien
        #设置位置
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_index #number_alien_x从0开始
        alien.rect.x = alien.x #设置rect的坐标
        alien.rect.y = alien_height + 2 * alien_height * row_index
        
        self.aliens.add(alien) #加入group
    
    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge(): #任意alien到达边缘就change_fleet_direction并break，因为游戏进行后alien被射击后是不规则的
                self._change_fleet_direction()
                break 
        
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed #整个alien group下移
        self.settings.fleet_direction *= -1 #反向
        
    def _alien_hit_ship(self):
        if self.stats.ship_life > 0:
            self.stats.ship_life -= 1 #注意这里不删除ship实例,只将ship_life -1
            self.scoreboard.prep_ships() #更新计数板
            self._reset_battle()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)  #unhide mouse when game is inactive
        
    def _alien_reach_bottom(self):
        for alien in self.aliens.sprites(): #获取sprite中每个成员
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._alien_hit_ship() #处理方法相同
                break #任意一个满足条件即退出for-loop
    
    def _reset_battle(self): #重置战场以复位alien和ship初始位置
        self.aliens.empty() #清空group
        self.bullets.empty()
        self._create_fleet() #重建alien
        self.ship.center_ship() #重新设置ship位置，看上去好像重建了ship实例，实际没有
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()