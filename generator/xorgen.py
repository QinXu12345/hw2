from __future__ import annotations
from .genbase import RandomGenBase
from ..typing import Uint32_t,Uint64_t

class Xnorgenerator(RandomGenBase):
    def __init__(self):
        super().__init__()
        
    def generate(self) -> int:
        if self._arc == 32:
            self._cur ^= (self._cur << Uint32_t(13)) & Uint32_t(0xffffffff)
            self._cur ^= self._cur >> Uint32_t(17)
            self._cur ^= (self._cur << Uint32_t(5)) & Uint32_t(0xffffffff)
        else:
            self._cur ^= (self._cur << Uint64_t(13)) & Uint64_t(0xffffffffffffffff)
            self._cur ^= self._cur >> Uint64_t(7)
            self._cur ^= (self._cur << Uint64_t(17)) & Uint64_t(0xffffffffffffffff)
        return self._cur.astype(Uint64_t) if RandomGenBase._arc == 64 else self._cur.astype(Uint32_t)
    