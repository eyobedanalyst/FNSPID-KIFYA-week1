# src/indicators.py

import pandas as pd


class Indicators:
    def __init__(self, prices: pd.DataFrame):
        self.prices = prices

    def returns(self):
        return self.prices.pct_change().dropna()

    def moving_average(self, window=20):
        return self.prices.rolling(window).mean()

    def volatility(self):
        return self.returns().std()

    def correlation_matrix(self):
        return self.returns().corr()
