from ..db import BASE
from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from decimal import Decimal
from typing import List, Optional
from sqlalchemy.orm import relationship, Mapped, mapped_column
import uuid

class Wallet(BASE):
    __tablename__ = "wallets"
    id: Mapped[uuid.UUID] = mapped_column("id", UUID, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column("user_id", ForeignKey("user.id"))
    amount: Mapped[Decimal] = mapped_column("amount", Numeric(precision=10, scale=2, asdecimal=True))
    
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="user_wallet")
    owner: Mapped["User"] = relationship(back_populates="wallet")
