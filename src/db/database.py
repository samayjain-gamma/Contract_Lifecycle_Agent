import sqlite3
from pathlib import Path

from src.core.exception import CustomException
from src.core.logger import logger

BASE_DIR = Path(__file__).resolve().parents[2]
DB_DIR = BASE_DIR / "data"
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "contracts.db"


def get_connection():
    try:
        logger.info("Creating a database")
        conn = sqlite3.connect(DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        logger.info("Databsae created successfully")
        return conn
    except Exception as e:
        logger.error("Error during database creation")
