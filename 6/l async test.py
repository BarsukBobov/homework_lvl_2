import asyncio

tasks = []


async def b(future):
    future.set_result("result")
    future.set_exception("exception")
    raise future.exception()


async def a():
    future = asyncio.Future()
    task = asyncio.create_task(b(future))
    await asyncio.sleep(1)
    print(await future)
    print(future.exception())


asyncio.run(a())
