from src.core.exception import CustomException
from src.core.logger import logger
from src.db.database import get_connection


def init_db():

    try:

        logger.info("Entered in to initialinzing table in a database")
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS contracts (
            contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
            contract_name TEXT UNIQUE NOT NULL,
            starting_date TEXT,
            ending_date TEXT,
            contract_status TEXT,
            description TEXT,
            email TEXT
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS deliverables (
            deliverable_id INTEGER PRIMARY KEY AUTOINCREMENT,
            deliverable_name TEXT NOT NULL,
            delivery_date TEXT,
            delivery_status TEXT,
            description TEXT,
            contract_id INTEGER,
            FOREIGN KEY (contract_id) REFERENCES contracts(contract_id)
        )
        """
        )

        conn.commit()
        conn.close()
        logger.info("Database created successfully")

    except Exception as e:
        logger.error("Error occured during initializing tables")
        raise CustomException(e)


if __name__ == "__main__":
    init_db()
