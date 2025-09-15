import pytest
import pandas as pd
from sqlalchemy import create_engine


@pytest.fixture
def sample_stock_df():
    """A small fake stock DataFrame for testing transforms & loads."""
    return pd.DataFrame({
        "Date": pd.date_range("2024-01-01", periods=5, freq="D"),
        "Open": [10, 11, 12, 13, 14],
        "High": [11, 12, 13, 14, 15],
        "Low": [9, 10, 11, 12, 13],
        "Close": [10.5, 11.5, 12.5, 13.5, 14.5],
        "Volume": [1000, 1100, 1200, 1300, 1400],
    })


@pytest.fixture
def in_memory_engine():
    """Provide a temporary in-memory SQLite engine for testing loads."""
    engine = create_engine("sqlite:///:memory:")
    yield engine
    engine.dispose()


@pytest.fixture
def fake_yf_history_df():
    """Fake Yahoo Finance history DataFrame."""
    return pd.DataFrame({
        "Open": [10, 11],
        "High": [12, 13],
        "Low": [9, 10],
        "Close": [11, 12],
        "Volume": [1000, 1100],
    }, index=pd.to_datetime(["2024-01-02", "2024-01-03"]))
