import unittest

from p_life_game.game_map import GameMap


class TestGameMap(unittest.TestCase):
    def setUp(self):
        self.g_map = GameMap()
        # print("start")

    def tearDown(self):
        # print("end")
        pass

    def test_reset(self):
        """测试随机生成的细胞数是否正确"""
        self.g_map.reset()

        expected_count = self.g_map.sets.rows * self.g_map.sets.cols * \
            self.g_map.sets.life_ratio

        count = 0

        for i in range(self.g_map.sets.rows):
            for j in range(self.g_map.sets.cols):
                if self.g_map.point_map[i][j] == 1:
                    count += 1

        self.assertEqual(expected_count, count)

    def test_get_neighbor_count(self):
        """测试(1, 1)的邻居数是否正确"""
        self.g_map.update_neighbors_map(0, 0, 1)
        self.g_map.point_map[0][0] = 1
        self.g_map.update_neighbors_map(0, 2, 1)
        self.g_map.point_map[0][2] = 1
        self.g_map.update_neighbors_map(2, 2, 1)
        self.g_map.point_map[2][2] = 1
        self.g_map.update_neighbors_map(2, 0, 1)
        self.g_map.point_map[2][0] = 1

        self.assertEqual(4, self.g_map.get_neighbor_count(1, 1))

    def test_set(self):
        """测试赋值是否成功"""

        self.g_map.set(0, 0, 1)

        self.assertEqual(1, self.g_map.point_map[0][0])

    def test_get(self):
        """测试读取的数据是否正确"""

        self.assertEqual(self.g_map.point_map[0][0], self.g_map.get(0, 0))

    def test_size(self):
        self.assertEqual(self.g_map.point_map.shape, (self.g_map.sets.rows,
                                                      self.g_map.sets.cols))


if __name__ == '__main__':
    unittest.main()
