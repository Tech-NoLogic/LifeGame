"""
该模块定义一个用于表示游戏地图并对地图进行查询更新的类
"""

import random as r
import numpy as np

from .settings import Settings


class GameMap():
    """用于表示游戏地图并对地图进行查询更新"""

    def __init__(self):
        """地图将在逻辑模块进行初始化"""

        self.sets = Settings()

        self.point_map = np.zeros((self.sets.rows, self.sets.cols), dtype=int)

        self.neighbors_map = np.zeros((self.sets.rows, self.sets.cols),
                             dtype=int)

    def update_neighbors_map(self, row, col, set_val):
        """更新邻居矩阵的值"""

        delta_row = [0, 1, 1, 1, 0, -1, -1, -1]
        delta_col = [1, 1, 0, -1, -1, -1, 0, 1]

        if self.point_map[row][col] == 0 and \
                set_val == 1:
            # 将[row][col]置活

            for i in range(8):
                new_row = row + delta_row[i]
                new_col = col + delta_col[i]

                if 0 <= new_row < self.sets.rows and \
                        0 <= new_col < self.sets.cols:

                        self.neighbors_map[new_row][new_col] += 1

        elif self.point_map[row][col] == 1 and \
                set_val == 0:
            # 将[row][col]置死

            for i in range(8):
                new_row = row + delta_row[i]
                new_col = col + delta_col[i]

                if 0 <= new_row < self.sets.rows and \
                        0 <= new_col < self.sets.cols:

                    self.neighbors_map[new_row][new_col] -= 1

        else:
            pass

    def set(self, row, col, val):
        """当游戏进行中，需要常常更新地图上方格的状态"""
        self.update_neighbors_map(row, col, val)
        self.point_map[row][col] = val

    def get(self, row, col):
        """当需要将游戏状态呈现给用户时，就需要获取地图上方格的状态"""
        return self.point_map[row][col]

    def reset(self):
        """重置地图并按life_ratio随机地填充一些活细胞"""
        life_ratio = self.sets.life_ratio

        self.point_map = np.zeros((self.sets.rows, self.sets.cols), dtype=int)
        point_count = self.sets.rows * self.sets.cols
        point_life_count = point_count * life_ratio

        point_now_count = 0

        while point_now_count < point_life_count:
            new_x = r.randint(0, self.sets.rows - 1)
            new_y = r.randint(0, self.sets.cols - 1)

            if self.get(new_x, new_y) == 0:
                point_now_count += 1
                self.set(new_x, new_y, 1)

    def get_neighbor_count(self, row, col):
        """地图上一个方格周围活细胞数是游戏逻辑里的重要数据"""
        """
        delta_row = [0, 1, 1, 1, 0, -1, -1, -1]
        delta_col = [1, 1, 0, -1, -1, -1, 0, 1]

        count_nei = 0

        for i in range(8):
            new_row = row + delta_row[i]
            new_col = col + delta_col[i]
            if 0 <= new_row < self.sets.rows and \
                    0 <= new_col < self.sets.cols and \
                    self.get(new_row, new_col) == 1:

                count_nei += 1

        return count_nei
        """
        return self.neighbors_map[row][col]
