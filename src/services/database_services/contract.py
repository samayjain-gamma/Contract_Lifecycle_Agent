from src.db.models import Contract
from src.db.session import SessionLocal


def insert_contract(contract_data):
    session = SessionLocal()
    try:
        contract = Contract(
            contract_name=contract_data["contract_name"],
            starting_date=contract_data["starting_date"],
            ending_date=contract_data["expiry_date"],
            contract_status=contract_data.get("contract_status", "Pending"),
            description=contract_data.get("description", ""),
            email=contract_data.get("email"),
        )

        session.add(contract)
        session.commit()
        session.refresh(contract)

        return contract.contract_id

    finally:
        session.close()
