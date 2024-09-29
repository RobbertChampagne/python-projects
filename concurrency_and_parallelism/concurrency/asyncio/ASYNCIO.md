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