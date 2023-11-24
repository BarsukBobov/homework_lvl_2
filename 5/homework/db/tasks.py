import asyncio

import asyncpg
from asyncpg import Record

from misc.db import init


async def run_async_fetch_from_db(db_config: dict, category_names: list[str]) -> tuple[list[Record]]:
    db_pool = await init(db_config)
    tasks = [asyncio.create_task(get_products_by_category_name(db_pool, category_name)) for category_name in category_names]
    return await asyncio.gather(*tasks)


async def get_products_by_category_name(conn: asyncpg.Pool, category_name: str) -> list[Record]:
    return await conn.fetch(
        f"""
        WITH RECURSIVE category_tree AS (
            SELECT id, name, parent_id
            FROM categories
            WHERE id = (SELECT id FROM categories where name = '{category_name}')
            UNION ALL
            SELECT c.id, c.name, c.parent_id
            FROM categories c
            JOIN category_tree ct ON ct.id = c.parent_id
        )
        SELECT p.name
        FROM products p
        JOIN category_tree ct ON p.category_id = ct.id;
        """
    )
