from typing import Optional

from pydantic import BaseModel

# Shared properties
class CompanyBase(BaseModel):
    name: Optional[str] = None
    legal_name: Optional[str] = None
    cnpj: Optional[str] = None
    is_active: Optional[bool] = True

# Properties to receive via API on creation
class CompanyCreate(CompanyBase):
    name: str
    legal_name: str
    cnpj: str

class CompanyUpdate(CompanyBase):
    pass

class CompanyInDBBase(CompanyBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Company(CompanyInDBBase):
    pass