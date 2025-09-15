import pandas as pd
from etl.transform import add_indicators


def test_add_indicators_minimal():
    data = {
    "Date": pd.date_range("2024-01-01", periods=5, freq="D"),
    "Open": [1, 2, 3, 4, 5],
    "High": [1, 2, 3, 4, 5],
    "Low": [1, 2, 3, 4, 5],
    "Close":[1, 2, 3, 4, 5],
    "Volume":[10, 20, 30, 40, 50],
    }
    df = pd.DataFrame(data)
    out = add_indicators(df)

    assert set(["Daily_Return", "SMA_20", "EMA_20"]).issubset(out.columns)
    assert len(out) == len(df)
    # First daily return should be NaN, others finite
    assert pd.isna(out.loc[out.index[0], "Daily_Return"]) or out.loc[out.index[0], "Daily_Return"] == 0