import profile

from p_life_game.game_map import GameMap


class ProfileTestGameMap():
    def __init__(self):
        self.g_map = GameMap()

    def profile_test_reset(self):
        self.g_map.reset()

    """
    def profile_test_get_neighbor_count(self):
        self.g_map.get_neighbor_count(1, 1)
    """


if __name__ == '__main__':
    pro_test = ProfileTestGameMap()

    profile.run("pro_test.profile_test_reset()")
    # profile.run("pro_test.profile_test_get_neighbor_count()")