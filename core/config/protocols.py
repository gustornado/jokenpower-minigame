from typing import Protocol

class Platform(Protocol):
    def now(self) -> int:
        ...
    
    def set_framerate(self) -> int:
        ...