# Multiprocessing 

Using the multiprocessing module allows you to create separate processes,<br>
each with its own Python interpreter and memory space, bypassing the GIL and enabling true parallelism.

A simple example that demonstrates how to use the multiprocessing module in Python to perform CPU-bound tasks in parallel.

`multiprocess.py`
```Python
# Function to perform a CPU-bound task
def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

# Worker function for multiprocessing
def worker(n):
    result = cpu_bound_task(n)
    print(f"Process {multiprocessing.current_process().name}, Result: {result}")

# Main function to start processes
def main():
    # Number of iterations for the CPU-bound task
    n = 10000000

    # Create and start processes
    processes = []
    for i in range(4):
        # A tuple containing the arguments to be passed to the worker function. 
        process = multiprocessing.Process(target=worker, args=(n,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

if __name__ == '__main__':
    main()
```

OUTPUT:
```Bash
Process Process-1, Result: 333333283333335000000
Process Process-2, Result: 333333283333335000000
Process Process-3, Result: 333333283333335000000
Process Process-4, Result: 333333283333335000000
```

---

### Synchronization in multiprocessing

we can use a **shared value** or array and **synchronize access** to it using a `multiprocessing.Lock`.<br>
This ensures that only one process can modify the shared data at a time.<br>
We'll also introduce random delays to simulate processes working on different tasks.<br>

Using `multiprocessing.Value` instead of a global variable is necessary because global variables are not shared between processes in Python.<br> 
Each process has its own memory space, so changes made to a global variable in one process will not be reflected in another process.

`multiprocessing.Value` provides a way to create a shared value that can be safely accessed and modified by multiple processes.<br> 
It ensures that the value is stored in shared memory, allowing all processes to see and update the same value.

`synchronizingMultiprocesses.py`
```Python

# Function to perform a CPU-bound task
def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

# Worker function for multiprocessing with synchronization
def worker(n, shared_value, lock):
    result = cpu_bound_task(n)
    time.sleep(random.uniform(0.1, 0.5))  # Simulate work with random delay
    with lock:
        shared_value.value += result
        print(f"Process {multiprocessing.current_process().name} updated shared value to {shared_value.value}")

# Main function to start processes
def main():
    # Number of iterations for the CPU-bound task
    n = 1000000

    # Shared value and lock for synchronization
    shared_value = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    # Create and start processes
    processes = []
    for i in range(4):
        process = multiprocessing.Process(target=worker, args=(n, shared_value, lock))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print(f"Final shared value: {shared_value.value}")

if __name__ == '__main__':
    main()
```

OUTPUT 1:
```Bash
Process Process-4 updated shared value to 584144992
Process Process-3 updated shared value to 1168289984
Process Process-1 updated shared value to 1752434976
Process Process-2 updated shared value to -1958387328
Final shared value: -1958387328
```

OUTPUT 2:
```Bash
Process Process-1 updated shared value to 584144992
Process Process-4 updated shared value to 1168289984
Process Process-2 updated shared value to 1752434976
Process Process-3 updated shared value to -1958387328
Final shared value: -1958387328
```