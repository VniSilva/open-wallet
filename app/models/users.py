from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import uuid
from db import BASE

class User(BASE):
    __tablename__ = "users"
    id : Mapped[uuid.UUID] = mapped_column("id", UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column("name", String(20), nullable=False)
    email: Mapped[str] = mapped_column("email", String(40), unique=True, nullable=False)
    password: Mapped[str] = mapped_column("password", String(250), nullable=False)
    created_at: Mapped[datetime] = mapped_column("created_at", DateTime, default=datetime.now())

    theme_id: Mapped[int] = mapped_column("theme_id", ForeignKey("userstheme.id"))
    theme: Mapped["UserTheme"] = relationship(back_populates="user", cascade="all, delete-orphan")

class UserTheme(BASE):
    __tablename__ = "userstheme"
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[uuid.UUID] = mapped_column("user_id", ForeignKey("users.id"))
    darkmode: Mapped[bool] = mapped_column("darkmode", Boolean, default=True)
    main_color: Mapped[str] = mapped_column("main_color", String(7), default="#54bad6")

    user = Mapped["User"] = relationship(back_populates="theme")

