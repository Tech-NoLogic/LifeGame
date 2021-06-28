"""
该模块定义一个用于根据游戏逻辑更新地图的类
"""

import numpy as np

from .game_map import GameMap
from .settings import Settings


class LifeGame():
    """用于根据游戏逻辑更新地图"""

    def __init__(self):
        """将在主程序中初始化实例"""
        self.g_map = GameMap()
        self.sets = Settings()

        self.g_map.reset()
        # self.fig, self.ax = plt.subplots()

    def _update(self):
        temp_map = np.copy(self.g_map.point_map)
        temp_neighbors_map = np.copy(self.g_map.neighbors_map)

        delta_row = [0, 1, 1, 1, 0, -1, -1, -1]
        delta_col = [1, 1, 0, -1, -1, -1, 0, 1]

        for i in range(self.sets.rows):
            for j in range(self.sets.cols):
                temp = self.g_map.get_neighbor_count(i, j)
                value = self.g_map.get(i, j)

                if value == 0 and temp == 3:
                    temp_map[i][j] = 1

                    for k in range(8):
                        new_r = i + delta_row[k]
                        new_c = j + delta_col[k]

                        if 0 <= new_r < self.sets.rows and \
                            0 <= new_c < self.sets.cols:
                            temp_neighbors_map[new_r][new_c] += 1

                elif value == 1 and temp >= 4:
                    temp_map[i][j] = 0

                    for k in range(8):
                        new_r = i + delta_row[k]
                        new_c = j + delta_col[k]

                        if 0 <= new_r < self.sets.rows and \
                                0 <= new_c < self.sets.cols:
                            temp_neighbors_map[new_r][new_c] -= 1

                elif value == 1 and temp <= 1:
                    temp_map[i][j] = 0

                    for k in range(8):
                        new_r = i + delta_row[k]
                        new_c = j + delta_col[k]

                        if 0 <= new_r < self.sets.rows and \
                                0 <= new_c < self.sets.cols:
                            temp_neighbors_map[new_r][new_c] -= 1

                else:
                    pass

        # print(self.g_map.neighbors_map)
        self.g_map.point_map = np.copy(temp_map)
        self.g_map.neighbors_map = np.copy(temp_neighbors_map)

    """
    def _draw(self):
        plt.cla()
        for i in range(self.sets.rows):
            for j in range(self.sets.cols):
                if self.g_map.get(i, j) == 1:
                    x = self.sets.row_space * i
                    y = self.sets.col_space * j

                    self.ax.scatter(x, y, s=self.sets.size_of_point)
    """

    def game_cycle(self):
        """进行一次游戏循环，将在此完成地图的更新 将在计时器触发时被调用"""
        self._update()
        # self._draw()
