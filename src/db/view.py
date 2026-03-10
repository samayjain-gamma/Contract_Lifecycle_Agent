import sqlite3
from pathlib import Path

# locate project root
BASE_DIR = Path(__file__).resolve().parents[2]

# database path
DB_PATH = BASE_DIR / "data" / "contracts.db"


def view_database():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # get all table names
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
    )

    tables = cursor.fetchall()

    for table in tables:

        table_name = table[0]

        print("\n" + "=" * 60)
        print(f"TABLE: {table_name}")
        print("=" * 60)

        # get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns_info = cursor.fetchall()

        column_names = [col[1] for col in columns_info]

        print("COLUMNS:")
        print(column_names)

        # fetch data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        print("\nDATA:")

        if not rows:
            print("No data found")
        else:
            for row in rows:
                print(row)

    conn.close()


if __name__ == "__main__":
    view_database()
