import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

import sys

sys.path.append('../backend')

from app.db.session import SessionLocal

from sqlalchemy.sql import text
from app.core.security import get_password_hash
import pandas as pd
from app.db.session import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        
        # df = pd.DataFrame()
        # df['login'] = ["admin"]
        # df['password_hash'] = [get_password_hash("321@ollopa")]
        # df['first_name'] = [None]
        # df['last_name'] = [None]
        # df['email'] = [None]
        # df['activated'] = [None]
        # df['lang_key'] = [None]
        # df['image_url'] = [None]
        # df['activation_key'] = [None]
        # df['reset_key'] = [None]
        # df['reset_date'] = [None]

        # df.to_sql("apo_user", con=engine, if_exists="append")
        db.execute(text("SELECT 1"))
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")




if __name__ == "__main__":
    main()
