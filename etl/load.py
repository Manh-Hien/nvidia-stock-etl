from pathlib import Path
from sqlalchemy import create_engine
import pandas as pd

from .utils import ensure_parent_dir, get_logger


logger = get_logger("load")



def to_sqlite(df: pd.DataFrame, sqlalchemy_url: str, table_name: str = "nvidia_stock") -> None:
    """Load the DataFrame into a SQLite table (replacing existing)."""
    if df is None or df.empty:
        raise ValueError("Refusing to load empty DataFrame.")


    if sqlalchemy_url.startswith("sqlite///"):
        db_path = Path(sqlalchemy_url.replace("sqlite:///", ""))
        ensure_parent_dir(db_path)


    engine = create_engine(sqlalchemy_url)
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    logger.info(f"Loaded {len(df)} rows into table '{table_name}'.")