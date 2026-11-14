import sys

import numpy as np
import pandas as pd


def test_environment() -> None:
    assert sys.version_info >= (3, 12)
    assert np.array([1, 2, 3]).sum() == 6
    frame = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    assert frame["a"].sum() == 3
