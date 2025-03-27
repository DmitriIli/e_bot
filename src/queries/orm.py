import asyncio
from sqlalchemy import text, insert
from database import session_factory
from models import Workers


async def insert_data():
    async with session_factory() as session:
        worker = Workers(username='Name')
        session.add(worker)
        await session.flush()
        await session.commit()
