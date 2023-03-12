from typing import List
from datetime import datetime

from sqlalchemy import Column , Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, relationship

from app.db.base_class import Base

class Company(Base):

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    legal_name = Column(String, index=True)
    cnpj = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime(timezone=True), server_default=datetime.now().isoformat())
    updated_at = Column(DateTime(timezone=True), server_default=datetime.now().isoformat())

    users: Mapped[List["User"]] = relationship()