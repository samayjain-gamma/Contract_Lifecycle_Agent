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


def modify_deliverable_status(deliverable_id: int):

    session = SessionLocal()

    deliverable = (
        session.query(Deliverable)
        .filter(Deliverable.deliverable_id == deliverable_id)
        .first()
    )

    if not deliverable:
        session.close()
        return None

    if deliverable.delivery_status == "Delivered":
        deliverable.delivery_status = "Pending"
    else:
        deliverable.delivery_status = "Delivered"

    session.commit()
    session.refresh(deliverable)
    session.close()

    return deliverable


if __name__ == "__main__":
    modify_deliverable_status(2)
