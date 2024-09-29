# Concurrency

**asyncio** is a concurrency framework in Python that allows you to write asynchronous code using async and await keywords.<br> 
It is designed for I/O-bound tasks and non-blocking operations. When using asyncio, tasks are executed concurrently, but not necessarily in parallel.<br> 
The event loop manages the execution of tasks, switching between them when they are waiting for I/O operations to complete.<br>

**`concurrency_and_parallelism/concurrency/concurrency.py`**
```Python
# Asynchronous function that simulates a delay and returns a value
async def delayed_print_and_return(value, delay):
    print(f"Starting task with value: {value}")
    await asyncio.sleep(delay) 
    print(f"Completed task with value: {value}")
    return value

# Asynchronous function that calls another function, waits, and returns a value
async def call_and_wait(value, delay):
    print(f"Calling delayed_print_and_return with value: {value} and delay: {delay}")
    result = await delayed_print_and_return(value, delay)
    print(f"Result from delayed_print_and_return: {result}")
    return result * 2
```
**Explanation:**

```Python
result = await delayed_print_and_return(value, delay)
```
- This line calls the asynchronous function **delayed_print_and_return(value, delay)** and waits for it to complete.
- The await keyword pauses the execution of the **call_and_wait** function until **delayed_print_and_return** finishes and returns a value.
- During this pause, the event loop can run other tasks, making efficient use of time.

```Python
await asyncio.sleep(delay) 
```
- This is awaited to simulate a delay within the **delayed_print_and_return** function. It allows the event loop to run other tasks during the delay.

OUTPUT:
```Bash
Calling delayed_print_and_return with value: 1 and delay: 1
Starting task with value: 1
Calling delayed_print_and_return with value: 2 and delay: 2
Starting task with value: 2
Calling delayed_print_and_return with value: 3 and delay: 3
Starting task with value: 3
Completed task with value: 1
Result from delayed_print_and_return: 1
Completed task with value: 2
Result from delayed_print_and_return: 2
Completed task with value: 3
Result from delayed_print_and_return: 3
Final result for value 1: 2
Final result for value 2: 4
Final result for value 3: 6
All CPU-bound tasks completed. Total time taken: 3.004685878753662 seconds.
```

# Sequential

- The main function runs each task one after another in a loop.
- Each task waits for the previous one to complete before starting.

OUTPUT:
```Bash
Calling delayed_print_and_return with value: 1 and delay: 1
Starting task with value: 1
Completed task with value: 1
Result from delayed_print_and_return: 1
Calling delayed_print_and_return with value: 2 and delay: 2
Starting task with value: 2
Completed task with value: 2
Result from delayed_print_and_return: 2
Calling delayed_print_and_return with value: 3 and delay: 3
Starting task with value: 3
Completed task with value: 3
Result from delayed_print_and_return: 3
Final result for value 1: 2
Final result for value 2: 4
Final result for value 3: 6
All CPU-bound tasks completed. Total time taken: 6.0081024169921875 seconds.
```