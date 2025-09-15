import logging
import os
import sys
from pathlib import Path


def get_logger(name: str = "etl") -> logging.Logger:
    """Create or return a configured logger."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        level = os.getenv("LOG_LEVEL", "INFO").upper()
        logger.setLevel(getattr(logging, level, logging.INFO))
        handler = logging.StreamHandler(sys.stdout)
        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.propagate = False
    return logger


def ensure_parent_dir(path: Path) -> None:
    """Ensure the parent directory for a file path exists."""
    path.parent.mkdir(parents=True, exist_ok=True)