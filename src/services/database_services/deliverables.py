from src.db.models import Deliverable
from src.db.session import SessionLocal


def insert_deliverables(contract_id, deliverables):

    session = SessionLocal()

    try:

        objects = [
            Deliverable(
                deliverable_name=d["deliverable_name"],
                delivery_date=d["delivery_date"],
                delivery_status=d.get("delivery_status", "Pending"),
                description=d.get("description", ""),
                contract_id=contract_id,
            )
            for d in deliverables
        ]

        session.add_all(objects)

        session.commit()

    finally:
        session.close()
