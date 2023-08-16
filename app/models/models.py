from sqlalchemy import BigInteger, Integer, Column, Table
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP
from sqlalchemy import Integer, String, Column, Boolean

from app.db.base_class import Base

class ApolloKPIReading(Base):
    __table__ = Table('apo_kpireadings', Base.metadata,
        Column('id', BigInteger, primary_key=True),
        Column('ts', TIMESTAMP, nullable=False),
        Column('plant_id', Integer, nullable=False),
        Column('asset_id', Integer, nullable=False),
        Column('readings', JSONB, nullable=False)
    )

class ApolloOMPReading(Base):
    __table__ = Table('apo_ompreadings', Base.metadata,
        Column('id', BigInteger, primary_key=True),
        Column('ts', TIMESTAMP, nullable=False),
        Column('plant_id', Integer, nullable=False),
        Column('asset_id', Integer, nullable=False),
        Column('readings', JSONB, nullable=False)
    )
    

class User(Base):
    __table__ = Table("apo_user",Base.metadata,
    Column('id',BigInteger, primary_key=True),
    Column('login',String(50), unique=True, nullable=False),
    Column('password_hash',String, nullable=False),
    Column('first_name',String(50), nullable=True),
    Column('last_name',String(50), nullable=True),
    Column('email',String, nullable=True),
    Column('activated',Boolean, nullable=True),
    Column('lang_key',String(6), nullable=True),
    Column('image_url',String[256],nullable=True ),
    Column('activation_key',String[20],nullable=True ),
    Column('reset_key',String[20],nullable=True ),
    Column('reset_date',TIMESTAMP,nullable=True ),
    extend_existing=True,
    )
    
    