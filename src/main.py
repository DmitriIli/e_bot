import asyncio
import sys
import os
from queries.core import async_connection, create_tables


sys.path.insert(1, os.path.join(sys.path[0], '..'))

asyncio.run(create_tables())