from sqlalchemy import text
from database import engine
from models import metadata_obj


async def async_connection():
    async with engine.connect() as conn:
        res = await conn.execute(text('SELECT VERSION()'))
        print('--------')
        print(f'{res.first()=}')


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.drop_all)
        await conn.run_sync(metadata_obj.create_all)
