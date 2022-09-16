# from core.config.protocols import Platform
from core.platform.platform_pygame import PlatformPygame as Platform
from core.match import Match
from core.config.types import KeyType
from core.aux.attack import Attack

class Game:
    def __init__(self, platform : Platform):
        self.platform = platform

    def start(self):
        while True:
            self.platform.check_exit()
            self.platform.draw_participants()

            self.platform.update_current_time()
            self.platform.check_player_attack()

            self.platform.update()
            self.platform.set_framerate(60)
