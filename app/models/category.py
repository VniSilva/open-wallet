from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import relationship, mapped_column, Mapped
from ..db import BASE
from typing import List

class Category(BASE):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column("name", String(length=20), nullable=False)
    color: Mapped[str] = mapped_column("color", String(length=7), nullable=False)

    transcation_categories: Mapped[List["TransactionCategory"]] = relationship(back_populates="category")