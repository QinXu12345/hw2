from __future__ import annotations
from abc import ABC,abstractmethod
import struct
import time

from ..typing import (
    Uint64_t,
    Uint32_t,
    Uint_t
)


class RandomGenBase(ABC):
    __slots__ = ['_cur']
    _arc: int = struct.calcsize("P") * 8 
    
    def __init__(self, base: RandomGenBase | None = None):
        if self._arc == 32:
            self._seed = Uint32_t(128)
        else:
            self._seed = Uint64_t(128)
            
        if base:
            self._cur = base._cur
        else:
            self._cur = self._seed 
            
    def set_seed(self, seed: Uint_t):
        self._seed = seed
        self._cur = self._seed
    
    @abstractmethod
    def generate(self) -> int:
        ...
    