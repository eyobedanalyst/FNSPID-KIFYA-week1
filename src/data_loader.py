# src/data_loader.py

import pandas as pd
from pathlib import Path


class DataLoader:
    def __init__(self, data_path="../data/"):
        self.data_path = Path(data_path)

    def load_stock(self, filename):
        file_path = self.data_path / filename
        return pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")

    def load_multiple(self, files):
        data = {}
        for f in files:
            name = f.replace(".csv", "")
            df = self.load_stock(f)
            data[name] = df["Close"]
        return data
