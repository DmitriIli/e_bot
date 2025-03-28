import asyncio
from sqlalchemy import text, insert
from models import WorkersORM
from database import session_factory, Base, engine


class AsyncORM:

    @staticmethod
    async def create_table():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_data():
        async with session_factory() as session:
            await asyncio.sleep(1)
            work = WorkersORM(user_name='Name')
            session.add(work)
            await session.flush()
            await session.commit()
