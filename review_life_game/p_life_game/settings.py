"""
该模块定义一个用于存储全局配置变量的类
"""


class Settings():
    """用于存储全局配置变量"""

    def __init__(self):
        self.rows = 80
        self.cols = 60

        self.row_space = 1  # 行距
        self.col_space = 1  # 列距

        self.size_of_point = 4

        self.interval = 0.005  # 更新时间间隔

        self.life_ratio = 0.1

        self.width = 8  # 显示的窗口宽度
        self.height = 6  # 显示的窗口高度
