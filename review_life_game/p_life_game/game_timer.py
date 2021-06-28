"""
该模块定义一个用于定时绘制游戏地图的类
"""

import matplotlib.pyplot as plt

from p_life_game.life_game import LifeGame
from p_life_game.settings import Settings


class GameTimer():
    """用于定时绘制游戏地图"""

    def __init__(self):
        """将在主程序中初始化实例 计时器以interval秒的频率触发
        trigger是个函数，计时器被触发时调用该函数 """
        self.li_game = LifeGame()
        self.sets = Settings()

        # self.fig, self.ax = plt.subplots()
        # plt.figure(figsize=(8, 6), dpi=80)

    def draw(self):
        """根据游戏地图画出散点图"""
        for i in range(self.sets.rows):
            for j in range(self.sets.cols):
                if self.li_game.g_map.get(i, j) == 1:
                    pos_x = self.sets.col_space * j
                    pos_y = self.sets.row_space * i
                    # print(f"<{x}, {y}>")
                    plt.scatter(pos_x, pos_y,
                                s=self.sets.size_of_point,
                                marker='s')

    def start(self):
        """启动计时器，之后将以interval秒的间隔持续触发"""
        plt.figure(figsize=(self.sets.width, self.sets.height))
        plt.xlim(-5 * self.sets.size_of_point,
                 self.sets.cols * self.sets.col_space +
                 5 * self.sets.size_of_point)
        plt.ylim(-5 * self.sets.size_of_point,
                 self.sets.rows * self.sets.row_space +
                 5 * self.sets.size_of_point)

        plt.ion()
        while True:
            plt.cla()
            self.li_game.game_cycle()
            self.draw()
            plt.pause(self.sets.interval)

        # plt.ioff()
        # plt.show()
