from sqlalchemy import String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import date
from decimal import Decimal
from typing import List
import uuid
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..db import BASE

class Transaction(BASE):
    __tablename__ = "transactions"
    id: Mapped[uuid.UUID] = mapped_column("id", UUID, primary_key=True, default=uuid.uuid4)
    amount: Mapped[Decimal] = mapped_column("amount", Numeric(precision=10, asdecimal=True, scale=2))
    transaction_date: Mapped[date] = mapped_column("date", Date, nullable=False, default=date.today)
    
    wallet_id: Mapped[uuid.UUID] = mapped_column("wallet_id", ForeignKey("wallets.id"))
    
    user_wallet: Mapped["Wallet"] = relationship(back_populates="transactions")
    transaction_categories : Mapped[List["TransactionCategories"]] = relationship(back_populates="transaction")