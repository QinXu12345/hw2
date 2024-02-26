import numpy as np
from numpy.typing import NDArray

TRIALS = 50000
START = 500
WIN = 1000
LOSS = 0

def run_gamble(
    trail: int = 50000,
    start: int | float = 500,
    win: int = 1000,
    loss: int = 0 
) -> NDArray:
    