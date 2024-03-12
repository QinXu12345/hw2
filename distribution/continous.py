from.distbase import DistBase, MEAN_TYPE, COV_TYPE
from ..typing import OFFSET,Float_t
from numpy.typing import NDArray
import numpy as np


class Uniform(DistBase):
    def __init__(
        self,
        loc:MEAN_TYPE = 0.0, 
        scale:COV_TYPE = 1.0
        ) -> None:
        super().__init__(loc, scale)
            
    def rvs(self, size: int | None = None) -> NDArray[Float_t]:
        if isinstance(size, int):
            assert size > 0
        rn = np.array([self._rng.generate() for _ in range(size)])
        norm_rn = rn / self._norm
        return 1 - (norm_rn - self._loc) / self._scale
    
    def var(self) -> Float_t:
        return 1/12 * (1 + self._loc)
    
class Exponential(DistBase):
    def __init__(
        self, 
        loc:MEAN_TYPE = 0.0, 
        scale:COV_TYPE = 1.0
        ) -> None:
        super().__init__(loc, scale)
        self._unif = Uniform(loc,scale)
        
    def rvs(self, size: int | None = None) -> NDArray[Float_t]:
        assert size > 0 and isinstance(size, int)
        uniform = self._unif.rvs(size)
        rn = np.log(uniform)
        return rn
    
    def var(self) -> Float_t:
        pass
class Normal(DistBase):
    def __init__(
        self,
        mean: MEAN_TYPE = 0.0,
        cov: COV_TYPE = 1.0
    ) -> None:
        super().__init__(mean, cov)
        self._unif = Uniform()
    
    def rvs(self,size: int | None = None) -> NDArray[Float_t]:
        std_norm = self._box_muller(self._scale.shape[0])
        lower_tri = np.linalg.cholesky(self._scale)
        return lower_tri @ std_norm + self._loc
    
    def var() -> Float_t:
        pass
        
    def _box_muller(self,size: int) -> NDArray[Float_t]:
        uniform_rvs1 = self._unif.rvs(size)
        uniform_rvs2 = self._unif.rvs(size)
        std_norm = np.sqrt(-2 * np.log(uniform_rvs1)) * np.cos(2 * np.pi * uniform_rvs2)
        return std_norm