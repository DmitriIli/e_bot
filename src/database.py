import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker,  DeclarativeBase
from sqlalchemy import create_engine
from config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)


session_factory = async_sessionmaker(engine)


class Base(DeclarativeBase):
    ...
