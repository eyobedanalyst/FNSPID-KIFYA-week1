# src/pipeline.py

from src.data_loader import DataLoader
from src.indicators import Indicators
from src.analytics import FinancialAnalytics


class StockPipeline:
    def __init__(self, files):
        self.loader = DataLoader()
        self.files = files

    def run(self):
        stock_data = self.loader.load_multiple(self.files)

        # Combine into DataFrame
        import pandas as pd
        combined = pd.concat(stock_data, axis=1)

        # Indicators
        ind = Indicators(combined)
        returns = ind.returns()
        ma20 = ind.moving_average(20)
        vol = ind.volatility()
        corr = ind.correlation_matrix()

        # Financial metrics per stock
        metrics = {}
        for col in combined.columns:
            fa = FinancialAnalytics(combined[col])
            metrics[col] = {
                "CAGR": fa.cagr(),
                "Sharpe": fa.sharpe(),
                "ReturnRate": fa.return_rate(),
            }

        return {
            "combined": combined,
            "returns": returns,
            "ma20": ma20,
            "volatility": vol,
            "correlation": corr,
            "metrics": metrics,
        }
