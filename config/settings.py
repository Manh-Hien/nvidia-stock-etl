from pathlib import Path


# Base directory of the repository
BASE_DIR = Path(__file__).resolve().parents[1]


# SQLite DB path (under /database)
DB_PATH = BASE_DIR / "database" / "nvidia_stock.db"


# SQLAlchemy connection URL for SQLite
SQLALCHEMY_URL = f"sqlite:///{DB_PATH}"


# ETL settings
TICKER = "NVDA"
HISTORY_PERIOD = "2y" # breadth of history to fetch
INTERVAL = "1d" # daily candles
INCLUDE_TODAY = True # try to include/refresh today's candle via intraday resample


# Logging
LOG_LEVEL = "INFO" # DEBUG/INFO/WARNING/ERROR