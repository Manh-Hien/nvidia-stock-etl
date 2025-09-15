import pandas as pd
from .utils import get_logger


logger = get_logger("transform")


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Add standard technical indicators to a sorted copy of the input DataFrame."""
    required = {"Date", "Open", "High", "Low", "Close", "Volume"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    out = df.sort_values("Date").copy()
    out["Daily_Return"] = out["Close"].pct_change()
    out["SMA_20"] = out["Close"].rolling(window=20, min_periods=1).mean()
    out["EMA_20"] = out["Close"].ewm(span=20, adjust=False).mean()
    return out