from sqlalchemy import BigInteger, Integer, Column, Table
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP

from app.db.base_class import Base

class ApolloOMPReading(Base):
    __table__ = Table('apo_ompreadings', Base.metadata,
        Column('id', BigInteger, primary_key=True),
        Column('ts', TIMESTAMP, nullable=False),
        Column('plant_id', Integer, nullable=False),
        Column('asset_id', Integer, nullable=False),
        Column('readings', JSONB, nullable=False),
        extend_existing=True,
    )
    