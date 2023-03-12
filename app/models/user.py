from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Boolean, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    image_url = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime(timezone=True), server_default=datetime.now().isoformat())
    updated_at = Column(DateTime(timezone=True), server_default=datetime.now().isoformat())
    
    student = relationship("Student", back_populates="user")

    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"), default=0)
    #company: Mapped["Company"] = relationship("Company", back_populates="company", foreign_keys=[company_id])


