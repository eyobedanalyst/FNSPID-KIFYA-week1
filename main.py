# main.py

from src.pipeline import StockPipeline

FILES = ["AAPL.csv", "META.csv", "GOOG.csv", "NVDA.csv", "MSFT.csv"]

pipeline = StockPipeline(FILES)
results = pipeline.run()

print(results["metrics"])
print(results["correlation"])
