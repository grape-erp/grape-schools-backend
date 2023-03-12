from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):


    def create(self, db: Session, *, obj_in: CompanyCreate) -> Company:
        db_obj = Company(
            name=obj_in.name,
            legal_name=obj_in.legal_name,
            cnpj=obj_in.cnpj,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj



    #TODO: Implementar atualização de empresas
    # def update(
    #     self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    # ) -> User:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     if update_data["password"]:
    #         hashed_password = get_password_hash(update_data["password"])
    #         del update_data["password"]
    #         update_data["hashed_password"] = hashed_password
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)




company = CRUDCompany(Company)
