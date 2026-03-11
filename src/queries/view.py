from sqlalchemy import text

from src.db.session import engine


def view_database():

    with engine.connect() as conn:

        tables = conn.execute(
            text("SELECT name FROM sqlite_master WHERE type='table'")
        ).fetchall()

        for table in tables:

            table_name = table[0]

            print("\n" + "=" * 60)
            print(f"TABLE: {table_name}")
            print("=" * 60)

            columns = conn.execute(text(f"PRAGMA table_info({table_name})")).fetchall()

            column_names = [col[1] for col in columns]

            print("Columns:", column_names)

            rows = conn.execute(text(f"SELECT * FROM {table_name}")).fetchall()

            print("Data:")
            for row in rows:
                print(row)


if __name__ == "__main__":
    view_database()
