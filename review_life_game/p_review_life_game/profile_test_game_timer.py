import profile

from game_timer import GameTimer


class ProfileTestGameTimer():
    def __init__(self):
        self.g_timer = GameTimer()

    def profile_test_draw(self):
        self.g_timer.draw()


if __name__ == '__main__':
    pro_test = ProfileTestGameTimer()

    profile.run('pro_test.profile_test_draw()')