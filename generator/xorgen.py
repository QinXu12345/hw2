from __future__ import annotations
from .genbase import RandomGenBase

class Xnorgenerator(RandomGenBase):
    def __init__(self):
        super().__init__()
        
    def generate(self) -> int:
        if self._arc == 32:
            self._cur ^= self._cur << 13
            self._cur ^= self._cur >> 17
            self._cur ^= self._cur << 5
        else:
            self._cur ^= self._cur << 13
            self._cur ^= self._cur >> 7
            self._cur ^= self._cur << 17
        return self._cur
    