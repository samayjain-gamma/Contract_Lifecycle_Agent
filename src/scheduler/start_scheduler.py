from apscheduler.schedulers.background import BackgroundScheduler

from src.core.logger import logger
from src.scheduler.contract_scheduler import (
    check_contract_expiry,
    check_overdue_deliverables,
)

scheduler = BackgroundScheduler()

scheduler.add_job(check_contract_expiry, "interval", days=1)
scheduler.add_job(check_overdue_deliverables, "interval", days=1)
jobs = scheduler.get_jobs()


def start_scheduler():
    logger.info("Entered into scheduler i.e. start_scheduler() ")
    logger.info(f"scheduler.get_jobs() : {jobs}")
    scheduler.start()
