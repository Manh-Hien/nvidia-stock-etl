# 📊 NVIDIA Stock ETL (SQLite)

An **end-to-end ETL pipeline** that extracts **NVIDIA (NVDA)** stock data, transforms it with technical indicators, and loads it into a **SQLite database**.

---

## 🚀 Features
- **ETL Pipeline**
  - Extracts daily NVDA stock data from Yahoo Finance (`yfinance`)
  - Ensures the latest trading day is included via intraday resampling
  - Transforms with technical indicators:
    - Daily returns
    - 20-day SMA (Simple Moving Average)
    - 20-day EMA (Exponential Moving Average)
  - Loads results into a **SQLite database**

- **Database Layer**
  - `database/nvidia_stock.db` automatically created
  - Query directly with Python, VS Code SQLite viewer, or DB Browser for SQLite

- **Automation & CI/CD**
  - GitHub Actions workflow runs ETL daily after US market close
  - Uploads SQLite database as a build artifact
  - Unit tests with **pytest**

- **Logging & Error Handling**
  - Clean logging instead of `print()`
  - Safe checks for empty dataframes and missing columns

---

## 🛠️ Tech Stack
- **Python 3.11+**
- **Pandas** + **yfinance**
- **SQLite** (via SQLAlchemy)
- **Pytest** (testing)
- **GitHub Actions** (automation)

---

## 📂 Project Structure
```bash
nvidia-stock-etl/
│── pipeline.py              # Main ETL entry point
│
│── config/                  # Configuration settings
│   ├── __init__.py
│   └── settings.py
│
│── etl/                     # Core ETL modules
│   ├── __init__.py
│   ├── utils.py             # Logging & helpers
│   ├── extract.py           # Stock extraction logic
│   ├── transform.py         # Add indicators (SMA, EMA, returns, etc.)
│   └── load.py              # Save data to SQLite
│
│── tests/                   # Unit tests
│   └── test_transform.py
│
│── database/                # SQLite database storage
│   └── (auto-created) nvidia_stock.db
│
│── .github/workflows/       # GitHub Actions CI/CD
│   └── ci.yml
│
│── requirements.txt         # Python dependencies
│── README.md
│── .gitignore
```


## ⚡ Quick Start

### 1️⃣ Clone repo
```bash
git clone https://github.com/Manh-Hien/nvidia-stock-etl.git
cd nvidia-stock-etl
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Run the ETL
```bash
python pipeline.py
```

## 🔍 Viewing the Database
### With Python
```python
import sqlite3, pandas as pd
conn = sqlite3.connect("database/nvidia_stock.db")
df = pd.read_sql("SELECT * FROM nvidia_stock LIMIT 5;", conn)
print(df)
```

### With VS Code

- Install the SQLite Viewer extension
- Right-click nvidia_stock.db → Open Database

## 🧪 Testing

### Run unit tests:
```bash
pytest -q
```

Built by Hien Anh Nguyen Manh