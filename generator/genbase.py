from __future__ import annotations
from abc import ABC,abstractmethod
import struct

class RandomGenBase(ABC):
    __slots__ = ['_cur']
    _seed: int = 0
    _arc: int = struct.calcsize("P") * 8 
    
    def __init__(self, base: RandomGenBase | None = None):
        if base:
            self._cur = base._cur
        else:
            self._cur = self._seed
            
    @classmethod
    def get_arg(cls):
        return cls._arc
            
    @classmethod
    def set_seed(cls,seed: int) -> int:
        cls._seed = seed
        
    @classmethod
    def get_seed(cls) -> int:
        return cls._seed
    
    @abstractmethod
    def generate(self) -> int:
        ...
    