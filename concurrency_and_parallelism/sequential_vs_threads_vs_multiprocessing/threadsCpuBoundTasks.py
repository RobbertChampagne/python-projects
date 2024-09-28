# python concurrency_and_parallelism/sequential_vs_threads_vs_multiprocessing/threadsCpuBoundTasks.py

# To illustrate the impact of the GIL on CPU-bound tasks, this simple example performs a CPU-intensive computation using multiple threads.
# This example will show that even though we create multiple threads, the GIL ensures that only one thread executes Python bytecode at a time, leading to no significant performance improvement.

import threading
import time

# Function to perform a CPU-bound task
def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

# Worker function for threading
def worker(n):
    start_time = time.time()
    result = cpu_bound_task(n)
    end_time = time.time()
    print(f"Result: {result}, Time taken: {end_time - start_time} seconds")

# Number of iterations for the CPU-bound task
n = 10**7

# Record the start time for the whole script
script_start_time = time.time()

# Create and start threads
threads = []
for i in range(4):
    thread = threading.Thread(target=worker, args=(n,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
    
# Record the end time for the whole script
script_end_time = time.time()

# Calculate and print the total time taken for the whole script
total_time = script_end_time - script_start_time
print(f"All CPU-bound tasks completed. Total time taken: {total_time} seconds.")