import asyncpg
import asyncio

from data import config
class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                password=config.PGPASSWORD,
                port=config.PGPORT,
                host=config.ip,
                database=config.PGDATABASE
            )
        )

loop = asyncio.get_event_loop()
db = Database(loop=loop)
