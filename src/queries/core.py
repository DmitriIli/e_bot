import asyncio
from sqlalchemy import text, insert
from database import engine
from models import metadata_obj, workers_table



async def create_tables():
    async with engine.begin() as conn:
        engine.echo = False
        await conn.run_sync(metadata_obj.drop_all)
        await conn.run_sync(metadata_obj.create_all)
        engine.echo = True


async def insert_data():
    async with engine.begin() as conn:
        await asyncio.sleep(1)
        # stmt = """ INSERT INTO workers(user_name) VALUES
        #         ('Jonh'),
        #         ('Karl'); """
        # await conn.execute(text(stmt))
        # await conn.commit() 
        
        stmt = insert(workers_table).values(
            [
                {"user_name":"Jonh"},
                {"user_name":"Karlito"},
            ]
        )
        await conn.execute(stmt)
        await conn.commit() 