from.distbase import DistBase
from ..typing import Float_t,OFFSET
from numpy.typing import NDArray
import numpy as np


class Uniform(DistBase):
    def __init__(
        self,
        loc:Float_t = 0.0, 
        scale:Float_t = 1.0
        ) -> None:
        super().__init__(loc, scale)
            
    def rvs(self, size: int) -> NDArray[Float_t]:
        assert size > 0 and isinstance(size, int)
        rn = np.array([self._rng.generate() for _ in range(size)])
        norm_rn = rn / self._norm
        return (norm_rn - self._loc) / self._scale
    
class Exponential(DistBase):
    def __init__(
        self, 
        loc:Float_t = 0.0, 
        scale:Float_t = 1.0
        ) -> None:
        super().__init__(loc, scale)
        self._unif = Uniform(loc,scale)
        
    def rvs(self, size: int) -> NDArray[Float_t]:
        assert size > 0 and isinstance(size, int)
        uniform = self._unif.rvs(size)
        rn = -np.log(uniform + OFFSET)
        return rn