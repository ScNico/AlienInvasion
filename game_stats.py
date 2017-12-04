# -*- coding: utf-8 -*-
# @Time  : 2017/12/4 13:19
# @Author: ScNico

class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        #游戏开始处于非活跃状态
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1