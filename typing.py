from __future__ import annotations
import numpy as np
from numpy.typing import NDArray
from typing import Iterable
import struct
import time

Uint64_t = np.uint64
Uint32_t = np.uint32

Float64_t = np.float64
Float32_t = np.float32

Float_t = Float64_t | Float32_t

Array64_t = NDArray[Uint64_t]
Array32_t = NDArray[Uint32_t]

Uint_t = Uint64_t | Uint32_t
Array_t = Array64_t | Array32_t

UMAX64 = np.iinfo(Uint64_t).max
UMAX32 = np.iinfo(Uint32_t).max

MOD64_C = np.iinfo(np.int32).max + 1
MOD32_C = np.iinfo(np.int16).max + 1


SEED = int(time.time())
PLATFORM = struct.calcsize("P") * 8  

OFFSET = 1e-5
Size = Iterable | int