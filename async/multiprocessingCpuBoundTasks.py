# python async/multiprocessingCpuBoundTasks.py

import multiprocessing
import time

# On Windows, the multiprocessing module uses the spawn method to start new processes, 
# which requires the if __name__ == '__main__': guard to ensure that the main module can be safely imported.
# To fix the issue, you need to wrap the code that starts the processes in an if __name__ == '__main__': block. 
# This ensures that the code is only executed when the script is run directly, not when it is imported as a module.

# Function to perform a CPU-bound task
def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

# Worker function for multiprocessing
def worker(n):
    start_time = time.time()
    result = cpu_bound_task(n)
    end_time = time.time()
    print(f"Result: {result}, Time taken: {end_time - start_time} seconds")

# Main function to start processes
def main():
    # Number of iterations for the CPU-bound task
    n = 10**7

    # Create and start processes
    processes = []
    for i in range(4):
        process = multiprocessing.Process(target=worker, args=(n,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All CPU-bound tasks completed.")

if __name__ == '__main__':
    main()