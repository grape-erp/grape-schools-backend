from sqlalchemy.orm import Session, registry

from app import crud, schemas
from app.core.config import settings
from app.db import base
from app.db.base_class import Base  # noqa: F401
from app.db.session import engine

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    Base.metadata.create_all(bind=engine)
    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)

    if not user:
        
        companies = crud.company.get_multi(db)
        if not companies:
            company_in = schemas.CompanyCreate(
                name="Empresa Teste",
                cnpj="35030474000160",
                legal_name="Empresa Teste do Teste"
            )

            company_db_obj = crud.company.create(db, obj_in=company_in)

        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            company_id=company_db_obj.id,
            is_superuser=True,
            name="Admin",
            last_name=""
        )
        crud.user.create(db, obj_in=user_in) 
