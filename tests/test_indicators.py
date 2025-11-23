import pandas as pd
from src.indicators import Indicators

def test_returns():
    data = pd.DataFrame({"A": [1, 2, 3, 4]})
    ind = Indicators(data)
    r = ind.returns()
    assert len(r) == 3
