from src.data_loader import DataLoader

def test_loader_path():
    loader = DataLoader()
    assert loader.data_path.exists()
