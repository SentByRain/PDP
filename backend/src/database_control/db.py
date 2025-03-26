from src.config import CONFIG
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(CONFIG.POSTGRESQL_DSN)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()