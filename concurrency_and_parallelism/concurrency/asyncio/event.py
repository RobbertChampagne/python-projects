# python concurrency_and_parallelism/concurrency/asyncio/event.py

import asyncio
import random

# Shared event
event = asyncio.Event()

# Asynchronous function to wait for the event
async def waiter(task_id):
    print(f"Task-{task_id} is waiting for the event")
    await event.wait()  # Wait for the event to be set
    
    # Simulate some work after receiving the event
    post_event_sleep = random.uniform(0.5, 1.5)
    print(f"Task-{task_id} received the event and is performing some work for {post_event_sleep:.2f} seconds")
    await asyncio.sleep(post_event_sleep)  # Simulate some work

    print(f"Task-{task_id} completed its work")

# Asynchronous function to set the event
async def setter():
    await asyncio.sleep(random.uniform(1, 3))  # Simulate some work
    print("Setting the event")
    event.set()  # Set the event

# Main function to run the tasks
async def main():
    # Create a list of waiter tasks
    waiters = [waiter(i) for i in range(1, 6)]
    
    # Create the setter task
    setter_task = setter()
    
    # Run the waiter tasks and the setter task concurrently
    await asyncio.gather(*waiters, setter_task)

if __name__ == "__main__":
    asyncio.run(main())