# The Python Global Interpreter Lock (GIL)
Is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously.<br> 
This lock is necessary because Python's memory management is not thread-safe.<br> 
The GIL ensures that only one thread executes Python bytecode at a time, even on multi-core systems.<br> 

### Key Points about the GIL
**Concurrency vs. Parallelism:**<br> 
- **Concurrency**:  Refers to the ability of a system to handle multiple tasks at the same time. It doesn't necessarily mean that the tasks are running simultaneously; rather, it means that the tasks are making progress concurrently. Concurrency is about dealing with lots of things at once.

- **Parallelism**: Multiple tasks run at exactly the same time on multiple processors or cores.
- The GIL allows for concurrency but limits parallelism in CPU-bound Python programs.

**Impact on Multi-threading:**<br> 
- The GIL can be a bottleneck in CPU-bound multi-threaded programs because it forces threads to execute one at a time.
- I/O-bound programs (e.g., web servers, network applications) are less affected by the GIL because they spend much of their time waiting for I/O operations, during which the GIL is released.

**Workarounds:**<br> 
- **Multi-processing**: Use the multiprocessing module to create separate processes, each with its own Python interpreter and memory space. This bypasses the GIL and allows true parallelism.
- **C Extensions**: Write performance-critical code in C or use Cython, which can release the GIL during long-running operations.
- **Alternative Implementations**: Use Python implementations that do not have a GIL, such as Jython (Python on the JVM) or IronPython (Python on the .NET framework).<br><br>

**GIL and Context Switching:**<br>

The GIL ensures only one thread executes Python bytecode at a time, but context switching allows threads to frequently take turns running, especially during I/O operations or when the GIL is released.

**Overlapping Execution:**<br>

Threads can overlap in execution due to context switching, reducing the total wall-clock time compared to the sum of individual thread times.

**Time Measurement:**<br>

Individual thread times include context switching and GIL waiting time, while total script time measures overall wall-clock time, which can be shorter due to overlapping execution.

**Context Switching vs. Thread Scheduling:**<br>

Context switching is the low-level operation of saving and restoring thread states, while thread scheduling is the high-level decision-making process of determining which thread runs when.<br><br>

---

### Sequential Execution VS Threads VS Multiprocessing:

**`sequentialExecutionCpuBoundTasks.py`**:<br>
Shows how you can run the same CPU-bound task sequentially without using threads or processes

```Bash
Result: 333333283333335000000, Time taken: 0.7686364650726318 seconds
Result: 333333283333335000000, Time taken: 0.7706217765808105 seconds
Result: 333333283333335000000, Time taken: 0.7706358432769775 seconds
Result: 333333283333335000000, Time taken: 0.7807185649871826 seconds
All CPU-bound tasks completed. Total time taken: 3.0906126499176025 seconds.
```

**`threadsCpuBoundTasks.py`**:<br>
To illustrate the impact of the GIL on CPU-bound tasks, this simple example performs a CPU-intensive computation using multiple threads.<br> 
This example will show that even though we create multiple threads, the GIL ensures that only one thread executes Python bytecode at a time, leading to no significant performance improvement.<br>
- **CPU-bound Tasks**: The GIL ensures that only one thread executes Python bytecode at a time,<br>
this means that using threads for CPU-bound tasks does not provide significant performance improvement over sequential execution.<br> 
Both approaches will effectively run the tasks one at a time, leading to similar execution times.<br><br>

```Bash
Result: 333333283333335000000, Time taken: 1.8848812580108643 seconds
Result: 333333283333335000000, Time taken: 2.000916004180908 seconds
Result: 333333283333335000000, Time taken: 1.9768507480621338 seconds
Result: 333333283333335000000, Time taken: 1.7888758182525635 seconds
All CPU-bound tasks completed. Total time taken: 2.0119190216064453 seconds.
```

**`multiprocessingCpuBoundTasks.py`**:<br>
Using the multiprocessing module allows you to create separate processes, each with its own Python interpreter and memory space, bypassing the GIL and enabling true parallelism.<br>

```Bash
Result: 333333283333335000000, Time taken: 0.631028413772583 seconds
Result: 333333283333335000000, Time taken: 0.6400279998779297 seconds
Result: 333333283333335000000, Time taken: 0.6550288200378418 seconds
Result: 333333283333335000000, Time taken: 0.6960282325744629 seconds
All CPU-bound tasks completed. Total time taken: 0.8020362854003906 seconds.
```

**Benefits of Using multiprocessing**
- **True Parallelism**: Each process runs independently, allowing multiple CPU-bound tasks to execute simultaneously on multiple CPU cores.
- **Improved Performance**: For CPU-bound tasks, using multiple processes can significantly reduce the overall execution time compared to using threads.<br><br>

---

### API calls with threads VS API calls with Asyncio:

**`threadsApiCalls.py`**:<br> 
Demonstrates how to use threads to make concurrent API calls using the httpx library in Python.<br> 
This example will fetch data from a public API concurrently using multiple threads.<br> 
However, it does not illustrate the impact of the Global Interpreter Lock (GIL) on CPU-bound tasks.<br><br> 
The GIL primarily affects CPU-bound tasks, where multiple threads are competing for CPU time to execute Python bytecode.<br> 
In the case of I/O-bound tasks, such as making API calls, the GIL is less of a bottleneck because the threads spend much of their time waiting for I/O operations to complete (e.g., waiting for a response from the server).<br> 
During these waiting periods, the GIL is released, allowing other threads to run.<br>

- **I/O-bound Tasks**: The GIL is less of a bottleneck because threads spend much of their time waiting for I/O operations, during which the GIL is released.<br><br>

```Bash
All API calls completed. Total time taken: 0.5280072689056396 seconds.
```

**`asyncApiCalls.py`**:<br> 
Demonstrates how to use asyncio to make concurrent API calls using the httpx library in Python.<br> 
This example will fetch data from a public API concurrently using asynchronous functions.<br> 
Unlike threads, asyncio does not involve the Global Interpreter Lock (GIL) in the same way, as it is designed for I/O-bound tasks and non-blocking operations.<br><br> 
asyncio is highly efficient because it allows the program to perform other tasks while waiting for I/O operations to complete (e.g., waiting for a response from the server).<br> 
During these waiting periods, the event loop can switch to other tasks, making efficient use of system resources.<br>

- **I/O-bound Tasks**: asyncio is highly efficient for I/O-bound tasks because it allows the program to perform other tasks while waiting for I/O operations, making efficient use of system resources.<br><br>

```Bash
All API calls completed. Total time taken: 0.38198161125183105 seconds.
```

**Which One is Better to Use?**<br> 
The choice between using threads and asyncio depends on your specific use case and requirements:

1. **Threads:**
    - **Pros:**
        - Easier to understand and use for those familiar with traditional multi-threading.
        - Can be used in scenarios where you need to leverage existing synchronous libraries that do not support asynchronous operations.
    - **Cons:**
        - Limited by the GIL for CPU-bound tasks, leading to no significant performance improvement.
        - Higher memory overhead due to the creation of multiple threads.
        - More complex error handling and synchronization mechanisms (e.g., locks, semaphores).
2. **Asyncio:**

    - **Pros:**
        - Highly efficient for I/O-bound tasks due to non-blocking operations.
        - Lower memory overhead compared to threads.
        - Simplified error handling and synchronization using async/await syntax.
    - **Cons:**
        - Steeper learning curve for those unfamiliar with asynchronous programming.
        - Requires libraries that support asynchronous operations (e.g., httpx instead of requests).

**Conclusion**:<br> 
- For **I/O-bound tasks** (e.g., making API calls, reading/writing files, network operations), asyncio is generally the better choice due to its efficiency and lower overhead.
- For **CPU-bound tasks** (e.g., heavy computations), neither threads nor asyncio will provide significant benefits due to the GIL. In such cases, consider using the multiprocessing module to achieve true parallelism.

In summary, for making concurrent **API calls, asyncio is typically more efficient** and should be preferred over threads, especially when dealing with a large number of I/O-bound operations.