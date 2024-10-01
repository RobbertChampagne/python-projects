# python concurrency_and_parallelism/concurrency/asyncio/lock.py

import asyncio
import random

# Shared resource
counter = 0

# Asynchronous function to increment the counter
async def increment_counter(lock, task_id):
    global counter
    # Simulate some asynchronous work before acquiring the lock
    pre_lock_sleep = random.uniform(0.5, 1.5)  # Output: A random float between 0.5 and 1.5
    print(f"Task-{task_id} is performing some work for {pre_lock_sleep:.2f} seconds before acquiring the lock")
    await asyncio.sleep(pre_lock_sleep)  # Simulate some work

    async with lock:
        print(f"Acquired lock: Task-{task_id}")
        temp = counter
        await asyncio.sleep(1)  # Simulate some work while holding the lock
        counter = temp + 1
        print(f"Counter incremented to {counter} by Task-{task_id}")
        print(f"Released lock: Task-{task_id}")

# Main function to run the tasks
async def main():
    lock = asyncio.Lock()
    
    # Create a list of tasks to run concurrently with explicit task IDs
    tasks = [increment_counter(lock, i) for i in range(1, 6)]
    
    # Run the tasks concurrently and wait for all of them to complete
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())