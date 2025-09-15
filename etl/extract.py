from datetime import datetime
import pandas as pd
import yfinance as yf


from .utils import get_logger


logger = get_logger("extract")




def _resample_intraday_to_daily(intraday: pd.DataFrame) -> pd.DataFrame:
    """Resample 1m/5m intraday OHLCV into a single daily candle."""
    if intraday.empty:
        return intraday
    intraday = intraday.copy()
    intraday.index = pd.to_datetime(intraday.index)
    # Remove timezone to align with history daily index
    intraday.index = intraday.index.tz_localize(None)


    daily = intraday.resample("1D").agg({
    "Open": "first",
    "High": "max",
    "Low": "min",
    "Close": "last",
    "Volume": "sum",
    "Dividends": "sum" if "Dividends" in intraday.columns else "sum",
    "Stock Splits": "sum" if "Stock Splits" in intraday.columns else "sum",
    })
    # Keep only last (today) row
    if not daily.empty:
        daily = daily.tail(1)
    return daily




def extract_stock_daily(ticker: str, period: str = "1y", interval: str = "1d", include_today: bool = True) -> pd.DataFrame:
    """
    Extract daily OHLCV from Yahoo Finance via yfinance.
    Optionally append/refresh today's candle using intraday data.
    """
    logger.info(f"Extracting {ticker} history: period={period} interval={interval}")


    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval, auto_adjust=False)
    if df is None or df.empty:
        raise RuntimeError("yfinance returned empty historical data.")


    # Normalize index timezone
    df.index = pd.to_datetime(df.index).tz_localize(None)


    if include_today:
        try:
            intraday = stock.history(period="1d", interval="1m", auto_adjust=False)
            daily_today = _resample_intraday_to_daily(intraday)
            if not daily_today.empty:
                daily_today.index = pd.to_datetime(daily_today.index).tz_localize(None)
                last_idx = daily_today.index[-1]
                if last_idx in df.index:
                    # Replace to ensure freshest values
                    df.loc[last_idx, ["Open", "High", "Low", "Close", "Volume"]] = \
                    daily_today.iloc[-1][["Open", "High", "Low", "Close", "Volume"]]
                else:
                    df = pd.concat([df, daily_today])
                    logger.info("Appended/refreshed today's candle from intraday data.")
        except Exception as e:
            logger.warning(f"Failed to append today's data from intraday: {e}")


    df.reset_index(inplace=True)
    df.rename(columns={"index": "Date", "Date": "Date"}, inplace=True)
    return df