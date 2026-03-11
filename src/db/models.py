from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Contract(Base):
    __tablename__ = "contracts"

    contract_id = Column(Integer, primary_key=True, autoincrement=True)
    contract_name = Column(String, nullable=False)
    starting_date = Column(String, nullable=False)
    ending_date = Column(String, nullable=False)
    contract_status = Column(String, default="Pending")
    description = Column(String, default="")
    email = Column(String, nullable=True)

    deliverables = relationship(
        "Deliverable", back_populates="contract", cascade="all, delete-orphan"
    )


class Deliverable(Base):
    __tablename__ = "deliverables"

    deliverable_id = Column(Integer, primary_key=True, autoincrement=True)
    deliverable_name = Column(String, nullable=False)
    delivery_date = Column(String, nullable=False)
    delivery_status = Column(String, default="Pending")
    description = Column(String, default="")
    contract_id = Column(Integer, ForeignKey("contracts.contract_id"), nullable=False)

    contract = relationship("Contract", back_populates="deliverables")
