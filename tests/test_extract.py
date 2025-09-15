import pandas as pd
from etl.extract import extract_stock_daily


def test_extract_uses_yfinance_mock(mocker, fake_yf_history_df):
    mock_ticker = mocker.patch("yfinance.Ticker")
    mock_ticker.return_value.history.return_value = fake_yf_history_df

    df = extract_stock_daily("NVDA", period="1d", interval="1d", include_today=False)

    assert not df.empty
    assert "Date" in df.columns