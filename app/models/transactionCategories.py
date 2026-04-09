from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..db import BASE
import uuid

class TransactionCategory(BASE):
    __tablename__ = "transactionCategories"
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column("category_id", ForeignKey("categories.id"))
    transaction_id: Mapped[uuid.UUID] = mapped_column("transaction_id", ForeignKey("transactions.id"))

    transaction: Mapped["Transaction"] = relationship(back_populates="transaction_categories")
    category: Mapped["Category"] = relationship(back_populates="transaction_categories")
