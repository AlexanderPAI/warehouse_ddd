from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import cfg
from infrastructure.models import Base

load_dotenv()

DB_URL = (
    f"postgresql+asyncpg://"
    f"{cfg.postgres_user}:{cfg.postgres_password}@{cfg.postgres_host}"
    f":{cfg.postgres_port}/{cfg.postgres_db}"
)

engine = create_async_engine(DB_URL)

session_factory = async_sessionmaker(bind=engine)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
