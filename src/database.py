import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)


async def async_connection():
    async with engine.connect() as conn:
        res = await conn.execute(text('SELECT VERSION()'))
        print(f'{res.first()=}')


asyncio.run(async_connection())
