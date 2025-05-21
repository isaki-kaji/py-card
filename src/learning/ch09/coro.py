import asyncio


async def heavy(name: str, sec: int) -> str:
    print(f"{name} start...")

    await asyncio.sleep(sec)
    print(f"{name} end...")
    return f"{name}: {sec}"
