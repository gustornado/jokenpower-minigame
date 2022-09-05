import pygame

class Platform:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
    
    def now(self) -> int:
        return pygame.time.get_ticks()
    
    def set_framerate(self, framerate: int) -> int:
        return self.clock.tick(framerate)