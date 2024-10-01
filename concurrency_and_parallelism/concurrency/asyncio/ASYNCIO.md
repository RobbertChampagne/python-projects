# ASYNCIO

## One task

### Waits for the function to complete before continuing.

When you use **await otherfunction()**, the current coroutine will pause and wait for **otherfunction()** to complete before continuing. <br>
This is useful when you need the result of **otherfunction()** to proceed with the next steps in your code.

`oneTask.py`
```Python
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
```

OUTPUT:
```Bash
Starting otherfunction
Completed otherfunction
Received: Result from otherfunction
```

---

## Multiple tasks

### Runs the function concurrently, allowing the current coroutine to continue executing.

When you use **asyncio.create_task(otherfunction())**, it schedules **otherfunction()** to run concurrently with the current coroutine.<br>
The current coroutine continues to execute without waiting for **otherfunction()** to complete.<br> This is useful when you want to run multiple tasks concurrently and don't need to wait for one to finish before starting another.

`multipleTasks.py`
```Python
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
```

OUTPUT:
```Bash
Continuing with other work while otherfunction runs
Starting otherfunction
Doing more work
Completed otherfunction
Received: Result from otherfunction
```

---

## Lock

### An `asyncio.Lock` is used to ensure that only one coroutine can access a shared resource at a time. 

This is useful when you have multiple coroutines that need to modify a shared resource and you want to prevent race conditions.

The use of `asyncio.Lock` becomes more meaningful when there are other asynchronous tasks or operations happening before acquiring the lock.<br> This allows other tasks to perform their operations concurrently while ensuring that access to the shared resource is synchronized.

**Summary**:
- **Concurrent Operations**: Tasks perform some asynchronous work concurrently before acquiring the lock.
- **Synchronized Access**: The lock ensures that only one task can access and modify the shared resource at a time.
- **Efficient Use of Time**: While one task is holding the lock, other tasks can perform their pre-lock operations, making efficient use of time.

`lock.py`
```Python
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
```

OUTPUT:
```Bash
Task-1 is performing some work for 0.55 seconds before acquiring the lock
Task-2 is performing some work for 1.28 seconds before acquiring the lock
Task-3 is performing some work for 1.12 seconds before acquiring the lock
Task-4 is performing some work for 0.84 seconds before acquiring the lock
Task-5 is performing some work for 0.70 seconds before acquiring the lock
Acquired lock: Task-1
Counter incremented to 1 by Task-1
Released lock: Task-1
Acquired lock: Task-5
Counter incremented to 2 by Task-5
Released lock: Task-5
Acquired lock: Task-4
Counter incremented to 3 by Task-4
Released lock: Task-4
Acquired lock: Task-3
Counter incremented to 4 by Task-3
Released lock: Task-3
Acquired lock: Task-2
Counter incremented to 5 by Task-2
Released lock: Task-2
```

---

## Semaphore

### An `asyncio.Semaphore `is used to control access to a shared resource by limiting the number of concurrent accesses.

It is useful when you want to limit the number of concurrent tasks that can access a particular resource, such as a network connection or a database.

A realistic example where tasks simulate uploading data to a database by adding a string to a shared list after an await operation. We'll use asyncio.Semaphore to limit the number of concurrent uploads.

`semaphore.py`
```Python
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
```

OUTPUT:
```Bash
Task-1 is performing some work for 0.55 seconds before acquiring the semaphore
Task-2 is performing some work for 0.64 seconds before acquiring the semaphore
Task-3 is performing some work for 0.95 seconds before acquiring the semaphore
Task-4 is performing some work for 1.04 seconds before acquiring the semaphore
Task-5 is performing some work for 1.46 seconds before acquiring the semaphore
Acquired semaphore: Task-1
Acquired semaphore: Task-2
Uploaded data from Task-1
Released semaphore: Task-1
Acquired semaphore: Task-3
Uploaded data from Task-3
Released semaphore: Task-3
Acquired semaphore: Task-4
Uploaded data from Task-2
Released semaphore: Task-2
Acquired semaphore: Task-5
Uploaded data from Task-4
Released semaphore: Task-4
Uploaded data from Task-5
Released semaphore: Task-5
Final upload list: ['Data from Task-1', 'Data from Task-3', 'Data from Task-2', 'Data from Task-4', 'Data from Task-5']
```

---

## Event

### An `asyncio.Event` allows one coroutine to signal an event and other coroutines to wait for that event to happen. 

`event.py`
```Python
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
```

OUTPUT:
```Bash
Task-1 is waiting for the event
Task-2 is waiting for the event
Task-3 is waiting for the event
Task-4 is waiting for the event
Task-5 is waiting for the event
Setting the event
Task-1 received the event and is performing some work for 1.18 seconds
Task-2 received the event and is performing some work for 1.03 seconds
Task-3 received the event and is performing some work for 1.08 seconds
Task-4 received the event and is performing some work for 0.67 seconds
Task-5 received the event and is performing some work for 1.29 seconds
Task-4 completed its work
Task-2 completed its work
Task-3 completed its work
Task-1 completed its work
Task-5 completed its work
```