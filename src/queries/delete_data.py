from src.db.models import Contract, Deliverable
from src.db.session import SessionLocal


def delete_all_data():

    session = SessionLocal()

    try:
        session.query(Deliverable).delete()

        session.query(Contract).delete()

        session.commit()

        print("All data deleted from contracts and deliverables.")

    except Exception as e:
        session.rollback()
        print("Error occurred:", e)

    finally:
        session.close()


if __name__ == "__main__":
    delete_all_data()
