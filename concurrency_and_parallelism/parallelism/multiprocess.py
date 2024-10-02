# python concurrency_and_parallelism/parallelism/multiprocess.py

import multiprocessing

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
        # In this case, it contains a single argument n
        # Can also contain multiple: args=(task_id, duration)
        process = multiprocessing.Process(target=worker, args=(n,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

if __name__ == '__main__':
    main()