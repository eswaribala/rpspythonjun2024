import asyncio
import random


async def producer(queue, data):
    for i in range(1, 5):
        data = data + data + random.randrange(100, 150)
        await queue.put(data)
        print(f"Producer {i} produced-> {data}")
        await asyncio.sleep(random.uniform(0.5, 1))


async def consumer(queue):
    while True:
        data = await queue.get()
        if data is None:
            break
        print(f"Consumer consumed {data}")
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue, random.randrange(5000,10000))) for i in range(5)]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.join()
    await queue.put(None)  # Signal the consumer to stop
    await consumer_task


# Run the event loop
asyncio.run(main())