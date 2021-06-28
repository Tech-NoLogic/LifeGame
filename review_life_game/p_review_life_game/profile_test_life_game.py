import profile

from p_life_game.life_game import LifeGame


class ProfileTestLifeGame():
    def __init__(self):
        self.li_game = LifeGame()

    def profile_test_game_cycle(self):
        self.li_game.game_cycle()


if __name__ == '__main__':
    pro_test = ProfileTestLifeGame()

    profile.run('pro_test.profile_test_game_cycle()')