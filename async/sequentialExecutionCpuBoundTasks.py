# python async/sequentialExecutionCpuBoundTasks.py

import time

# Function to perform a CPU-bound task
def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

# Worker function for sequential execution
def worker(n):
    start_time = time.time()
    result = cpu_bound_task(n)
    end_time = time.time()
    print(f"Result: {result}, Time taken: {end_time - start_time} seconds")

# Number of iterations for the CPU-bound task
n = 10**7

# Run the task sequentially
for i in range(4):
    worker(n)

print("All CPU-bound tasks completed.")