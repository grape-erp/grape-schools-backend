from typing import TYPE_CHECKING
from datetime import datetime


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Boolean, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Student(Base):

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)

    created_at = Column(DateTime(timezone=True), server_default=datetime.now().isoformat())
    updated_at = Column(DateTime(timezone=True), server_default=datetime.now().isoformat())

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="student", foreign_keys=[user_id])
