from __future__ import annotations
from .genbase import RandomGenBase
from numbers import Real

class LCGenerator(RandomGenBase):
    _a = 2 ** RandomGenBase._arc << 1
    _b = 2 ** RandomGenBase._arc << 2
    _module = 2 ** RandomGenBase._arc
    
    def __init__(self, a: int | None = None, b: int | None = None):
        super().__init__()
        if a and b:
            if a < 0 or b < 0:
                raise ValueError(f"""The values {a} and {b} cannot be negative""")
            self._a = a
            self._b = b
        else:
            raise ValueError(f"""The values a or/and b are None""")
        
    def generate(self) -> int:
        self._cur = (self._a * self._cur + self._b) % self._module
        return self._cur
        
    
    