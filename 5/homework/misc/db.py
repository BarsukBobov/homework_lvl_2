import json
from datetime import datetime, date
from typing import Any

import asyncpg


def json_serial(obj) -> Any:
    if isinstance(obj, datetime) or isinstance(obj, date):
        return obj.isoformat()

    if isinstance(obj, list):
        return str(obj)

    raise TypeError(f"Type {type(obj)} not serializable")


def dumps_default(obj: Any) -> str:
    return json.dumps(obj, default=json_serial)


async def init_connection(conn: asyncpg.Connection) -> asyncpg.Connection:
    await conn.set_type_codec(
        typename='jsonb',
        encoder=dumps_default,
        decoder=json.loads,
        schema='pg_catalog'
    )
    return conn


async def init(config: dict) -> asyncpg.Pool:
    dsn = config.get('dsn')
    if not dsn:
        raise RuntimeError('DB connection parameters not defined')
    return await asyncpg.create_pool(
        dsn=dsn,
        init=init_connection
    )
