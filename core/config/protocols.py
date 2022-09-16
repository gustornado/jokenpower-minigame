from typing import Protocol

class Platform(Protocol):
    def exit_check(self):
        ...
    
    def update(self):
        ...

    def now(self) -> int:
        ...
    
    def set_framerate(self) -> int:
        ...
    