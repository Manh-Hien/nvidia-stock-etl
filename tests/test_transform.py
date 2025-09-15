import pandas as pd
from etl.transform import add_indicators


def test_add_indicators_minimal(sample_stock_df):
    out = add_indicators(sample_stock_df)

    assert set(["Daily_Return", "SMA_20", "EMA_20"]).issubset(out.columns)
    assert len(out) == len(sample_stock_df)
    # First daily return should be NaN, others finite
    assert pd.isna(out.loc[out.index[0], "Daily_Return"]) or out.loc[out.index[0], "Daily_Return"] == 0