# -*- coding: utf-8 -*-
# @Time  : 2017/12/4 13:19
# @Author: ScNico

class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        #游戏开始处于活动状态
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit