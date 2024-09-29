# python concurrency_and_parallelism/concurrency/asyncio/oneTask.py

import asyncio

async def otherfunction():
    print("Starting otherfunction")
    await asyncio.sleep(2)
    print("Completed otherfunction")
    return "Result from otherfunction"

async def main():
    result = await otherfunction()
    print(f"Received: {result}")

if __name__ == "__main__":
    asyncio.run(main())