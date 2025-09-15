import os

from config.settings import (
    SQLALCHEMY_URL,
    TICKER,
    HISTORY_PERIOD,
    INTERVAL,
    INCLUDE_TODAY,
    LOG_LEVEL)
from etl.extract import extract_stock_daily
from etl.transform import add_indicators
from etl.load import to_sqlite
from etl.utils import get_logger


# Ensure logging level picked up by utils.get_logger
os.environ["LOG_LEVEL"] = LOG_LEVEL
logger = get_logger("pipeline")


def run() -> None:
    logger.info("Starting ETL pipeline…")
    df = extract_stock_daily(TICKER, HISTORY_PERIOD, INTERVAL, INCLUDE_TODAY)
    df = add_indicators(df)
    to_sqlite(df, SQLALCHEMY_URL, table_name="nvidia_stock")
    logger.info("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run()