import asyncio
import aiohttp
import time

async def job(i):
    print("Start Job", i)
    await asyncio.sleep(i)
    print("Job", i, "takes", i, " s")

async def main(loop):
    tasks = [loop.create_task(job(i)) for i in range(1, 3)]
    await asyncio.wait(tasks)

if __name__ == "__main__":
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
    print("Asyncio : " + str(time.time() - t1))