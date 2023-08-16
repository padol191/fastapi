import logging
from sqlalchemy.orm import Session

from app.crud import *
from app.schemas import *

from app.db import base  # noqa: F401
from app.core.config import settings

logger = logging.getLogger(__name__)



# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
from app.models.user import User

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    if settings.FIRST_USER:
        user = crud_user.get_by_login(db, login=settings.FIRST_USER)
        if not user:
            user_in = UserCreate(
                login=settings.FIRST_USER,
                activated=True,
                password_hash=settings.FIRST_USER_PW,
                first_name="Apollo",
                last_name="Apollo",
            )
            user = crud_user.create(db, obj_in=user_in)  # noqa: F841
        else:
            logger.warning(
                "Skipping creating first user. User with login name "
                f"{settings.FIRST_USER} already exists. "
            )
    else:
        logger.warning(
            "Skipping creating first user.  FIRST_USER needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_USER=admin"
        )
