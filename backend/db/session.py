from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

#SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
#engine=create_engine(SQLALCHEMY_DATABASE_URL )

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

sessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)