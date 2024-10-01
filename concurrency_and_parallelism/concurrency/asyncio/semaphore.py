# python concurrency_and_parallelism/concurrency/asyncio/semaphore.py

import asyncio
import random

# Shared resource
upload_list = []

# Asynchronous function to simulate uploading data to a database
async def upload_data(semaphore, task_id):
    # Simulate some asynchronous work before acquiring the semaphore
    pre_semaphore_sleep = random.uniform(0.5, 1.5)
    print(f"Task-{task_id} is performing some work for {pre_semaphore_sleep:.2f} seconds before acquiring the semaphore")
    await asyncio.sleep(pre_semaphore_sleep)  # Simulate some work

    async with semaphore:
        print(f"Acquired semaphore: Task-{task_id}")
        # Simulate uploading data to a database
        upload_sleep = random.uniform(0.5, 1.5)
        await asyncio.sleep(upload_sleep)  # Simulate upload time
        upload_list.append(f"Data from Task-{task_id}")
        print(f"Uploaded data from Task-{task_id}")
        print(f"Released semaphore: Task-{task_id}")

# Main function to run the tasks
async def main():
    # Create an asyncio semaphore with a limit of 2 concurrent accesses
    semaphore = asyncio.Semaphore(2)
    
    # Create a list of tasks to run concurrently with explicit task IDs
    tasks = [upload_data(semaphore, i) for i in range(1, 6)]
    
    # Run the tasks concurrently and wait for all of them to complete
    await asyncio.gather(*tasks)

    # Print the final upload list
    print("Final upload list:", upload_list)

if __name__ == "__main__":
    asyncio.run(main())