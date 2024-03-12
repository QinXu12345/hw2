from abc import ABC, abstractmethod
from ..generator import RandomGenBase
from ..generator import Xnorgenerator, LCGenerator
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

MEAN_TYPE = Float_t | NDArray[Float_t] | NDArray[Uint_t]

COV_TYPE = Float_t | NDArray[Float_t] | NDArray[Uint_t]

class DistBase(ABC):
    def __init__(
            self,
            loc:MEAN_TYPE = 0.0, 
            scale:MEAN_TYPE = 1.0
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
    def rvs(self, size: int | None = None) -> NDArray[Float_t]:
        ...
        
    @abstractmethod
    def var() -> Float_t:
        ...
        
    