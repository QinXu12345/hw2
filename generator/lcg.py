from __future__ import annotations
from ..typing import (
    Uint64_t,
    Uint32_t,
    Uint_t,
    MOD64_C,
    MOD32_C
)

from .genbase import RandomGenBase

class LCGenerator(RandomGenBase):
    _a: Uint_t = (
        Uint64_t(1103515245) if RandomGenBase._arc == 64 
        else Uint32_t(1103515245)
        )
    _b: Uint_t = (
        Uint64_t(12345) if RandomGenBase._arc == 64 
        else Uint32_t(12345)
        )
    _module: Uint_t = (
        MOD64_C if RandomGenBase._arc == 64 
        else MOD32_C
        )
    
    def __init__(
        self, a:  Uint_t | None = None, 
        b: Uint_t | None = None
        ):
        super().__init__()
        if a and b:
            if a < 0 or b < 0:
                raise ValueError(f"""The values {a} and {b} cannot be negative""")
            self._a = a
            self._b = b
        
    def generate(self) -> int:
        self._cur = (self._a * self._cur + self._b) % self._module
        return self._cur.astype(Uint64_t) if RandomGenBase._arc == 64 else self._cur.astype(Uint32_t)
        
    
    