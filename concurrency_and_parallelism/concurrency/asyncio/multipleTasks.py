# python concurrency_and_parallelism/concurrency/asyncio/multipleTasks.py

import asyncio

async def otherfunction():
    print("Starting otherfunction")
    await asyncio.sleep(2)
    print("Completed otherfunction")
    return "Result from otherfunction"

async def main():
    task = asyncio.create_task(otherfunction())
    print("Continuing with other work while otherfunction runs")
    await asyncio.sleep(1)
    print("Doing more work")
    result = await task
    print(f"Received: {result}")

if __name__ == "__main__":
    asyncio.run(main())