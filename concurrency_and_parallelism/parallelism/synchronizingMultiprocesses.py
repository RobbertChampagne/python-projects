# python concurrency_and_parallelism/parallelism/synchronizingMultiprocesses.py

import multiprocessing
import time
import random

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