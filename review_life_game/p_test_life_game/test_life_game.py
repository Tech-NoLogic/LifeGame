import unittest
from p_life_game.life_game import LifeGame
# import numpy as np
from mock import Mock, patch


class TestLifeGame(unittest.TestCase):
    def setUp(self):
        self.li_game = LifeGame()

    """
    def test_game_cycle(self):
        #测试一轮更新有没有更新正确
        self.li_game.g_map.point_map = np.zeros((self.li_game.sets.rows,
                                                 self.li_game.sets.cols),
                                                dtype=int)  # 将矩阵置零

        self.li_game.g_map.point_map[0][0] = 1
        self.li_game.g_map.point_map[0][2] = 1
        self.li_game.g_map.point_map[2][2] = 1
        # [1][1]周围的三个细胞

        self.li_game.g_map.point_map[1][3] = 1
        self.li_game.g_map.point_map[2][3] = 1
        self.li_game.g_map.point_map[3][3] = 1
        self.li_game.g_map.point_map[3][2] = 1
        self.li_game.g_map.point_map[3][1] = 1
        # [2][2]周围的五个细胞

        self.li_game.game_cycle()

        self.assertEqual(1, self.li_game.g_map.point_map[1][1]) 
        # 死细胞周围三个活的细胞变活
        self.assertEqual(0, self.li_game.g_map.point_map[2][2]) 
        # 活细胞周围大于三个活细胞变死
        self.assertEqual(0, self.li_game.g_map.point_map[0][0]) 
        # 活细胞周围少于两个活细胞变死
        self.assertEqual(0, self.li_game.g_map.point_map[0][1]) 
        # 不属于上面三种情况，保持不变
    """

    @patch('p_life_game.game_map.GameMap.get_neighbor_count',
                    new=Mock(return_value=3))
    @patch('p_life_game.game_map.GameMap.get',
                    new=Mock(return_value=0))
    def test_game_cycle_dead_with_three_living(self):
        """检验死细胞周围三个活细胞变活"""
        self.li_game.game_cycle()
        self.assertEqual(1, self.li_game.g_map.point_map[0][0])

    @patch('p_life_game.game_map.GameMap.get_neighbor_count',
                    new=Mock(return_value=4))
    @patch('p_life_game.game_map.GameMap.get',
                    new=Mock(return_value=1))
    def test_game_cycle_living_with_over_three_living(self):
        """检验活细胞周围三个以上活细胞变死"""
        self.li_game.game_cycle()
        self.assertEqual(0, self.li_game.g_map.point_map[0][0])

    @patch('p_life_game.game_map.GameMap.get_neighbor_count',
           new=Mock(return_value=1))
    @patch('p_life_game.game_map.GameMap.get',
           new=Mock(return_value=1))
    def test_game_cycle_living_with_under_two_living(self):
        """检验活细胞周围两个以下活细胞变死"""
        self.li_game.game_cycle()
        self.assertEqual(0, self.li_game.g_map.point_map[0][0])

    @patch('p_life_game.game_map.GameMap.get_neighbor_count',
           new=Mock(return_value=1))
    @patch('p_life_game.game_map.GameMap.get',
           new=Mock(return_value=0))
    def test_game_cycle_nothing_happened(self):
        """检验其他情况保持原状"""
        self.li_game.game_cycle()
        self.assertEqual(0, self.li_game.g_map.point_map[0][0])


if __name__ == '__main__':
    unittest.main()

