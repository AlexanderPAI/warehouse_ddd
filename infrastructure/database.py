from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///warehouse.db"

engine = create_engine(DATABASE_URL)

session_factory = sessionmaker(bind=engine)
