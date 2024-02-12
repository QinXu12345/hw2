from abc import ABC, abstractmethod
from ..generator import RandomGenBase
from ..generator import LCGenerator
from ..typing import (
    NDArray,
    Float_t,
    UMAX64,
    UMAX32,
    MOD64_C,
    MOD32_C,
    PLATFORM,
    Uint_t
)
import numpy as np

class DistBase(ABC):
    def __init__(
            self,
            loc:Float_t = 0.0, 
            scale:Float_t = 1.0
        ) -> None:
        super().__init__()
        self._rng = LCGenerator()
        self._loc = loc
        self._scale = scale
        if isinstance(self._rng,LCGenerator):
            self._norm = MOD64_C if PLATFORM == 64 else MOD32_C
        else:
            self._norm = UMAX64 if PLATFORM == 64 else UMAX32
        
    def switch_rng(self, rng: RandomGenBase):
        assert isinstance(rng, RandomGenBase)
        self._rng = rng
        if isinstance(self._rng,LCGenerator):
            self._norm = MOD64_C if PLATFORM == 64 else MOD32_C
        else:
            self._norm = UMAX64 if PLATFORM == 64 else UMAX32
            
    def set_seed(self, seed: Uint_t):
        return self._rng.set_seed(seed)
        
    @abstractmethod
    def rvs(self, size: int) -> NDArray[Float_t]:
        ...
        
    