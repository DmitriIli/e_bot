import asyncio
import sys
import os
from queries.core import async_connection, create_tables, insert_date


sys.path.insert(1, os.path.join(sys.path[0], '..'))

# asyncio.run(create_tables())
# asyncio.run(insert_date())



async def main():
    if __name__ == '__main__':
        task1 = asyncio.create_task(create_tables())
        task2 = asyncio.create_task(insert_date())
        await task1
        await task2

asyncio.run(main())