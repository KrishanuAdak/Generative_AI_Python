from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql+psycopg://iamkrishanu:12345678@localhost:5432/employee_db"

# Create Engine
engine=create_engine(DATABASE_URL,pool_pre_ping=True)

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()


