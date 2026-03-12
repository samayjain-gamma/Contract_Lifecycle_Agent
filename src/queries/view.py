from sqlalchemy import inspect, text

from src.db.session import engine


def view_database():
    """
    this function is to view the database in terminal
    """

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


def view_database_route():
    """
    this function is used by the router
    """

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    database_data = {}

    with engine.connect() as conn:

        for table in tables:

            columns = inspector.get_columns(table)
            column_names = [col["name"] for col in columns]

            result = conn.execute(text(f"SELECT * FROM {table}"))
            rows = [dict(row._mapping) for row in result.fetchall()]

            database_data[table] = {"columns": column_names, "rows": rows}
    print(database_data)
    return database_data


if __name__ == "__main__":
    view_database()
