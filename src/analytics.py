# src/analytics.py

import pynance as pn
import pandas as pd


class FinancialAnalytics:
    def __init__(self, prices: pd.Series):
        self.prices = prices.dropna()
        self.returns = self.prices.pct_change().dropna()

    def cagr(self):
        return pn.analysis.cagr(self.returns)

    def sharpe(self):
        return pn.analysis.sharpe(self.returns)

    def return_rate(self):
        return pn.analysis.return_rate(self.returns)
