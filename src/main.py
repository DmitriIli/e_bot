import asyncio
import sys
import os
from queries.orm import insert_data, create_table


sys.path.insert(1, os.path.join(sys.path[0], '..'))

# asyncio.run(create_tables())
# asyncio.run(insert_date())


async def main():
    if __name__ == '__main__':
        task1 = asyncio.create_task(create_table())
        task2 = asyncio.create_task(insert_data())
        await task1
        await task2


asyncio.run(main())
