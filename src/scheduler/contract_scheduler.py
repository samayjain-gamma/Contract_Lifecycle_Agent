from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from src.core.logger import logger
from src.db.models import Contract, Deliverable
from src.db.session import SessionLocal
from src.scheduler.mail_service import send_email


def check_contract_expiry():

    logger.info("Entered into check_contract_expiry()")
    session: Session = SessionLocal()

    today = datetime.today().date()
    threshold = today + timedelta(days=7)

    contracts = session.query(Contract).all()

    for contract in contracts:

        expiry = datetime.strptime(contract.ending_date, "%Y-%m-%d").date()
        logger.info(f"expiry date type : {type(expiry)}")
        if today <= expiry <= threshold:
            send_email(
                to_email=contract.email,
                subject="Contract Expiry Reminder",
                body=f"""
Contract : {contract.contract_name}

This is to remind you that
Your contract will expire on {contract.ending_date}
Please review and renew it ASAP
Aapka Apna
    SUKH KA SAATHI
    DUKH KA DAATA
""",
            )
    session.close()


def check_overdue_deliverables():

    session: Session = SessionLocal()

    today = datetime.today().date()

    contracts = session.query(Contract).all()
    deliverables = session.query(Deliverable).all()

    for contract in contracts:
        for d in deliverables:
            delivery_date = datetime.strptime(d.delivery_date, "%Y-%m-%d").date()

            if delivery_date == today and d.delivery_status != "Delivered":
                send_email(
                    to_email=contract.email,
                    subject="Alert: Last delivery date",
                    body=f"""
Deliverable: {d.deliverable_name}

Delivery date: {d.delivery_date}

Status: Overdue
""",
                )

            if delivery_date < today and d.delivery_status != "Delivered":
                send_email(
                    to_email=contract.email,
                    subject="Deliverable Overdue",
                    body=f"""
Deliverable: {d.deliverable_name}

Delivery date: {d.delivery_date}

Status: Overdue
""",
                )

    session.close()
