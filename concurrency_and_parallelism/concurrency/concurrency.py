# python concurrency_and_parallelism/concurrency/concurrency.py

import asyncio
import time

# Asynchronous function that simulates a delay and returns a value
async def delayed_print_and_return(value, delay):
    print(f"Starting task with value: {value}")
    await asyncio.sleep(delay)  # Simulate a delay
    print(f"Completed task with value: {value}")
    return value

# Asynchronous function that calls another function, waits, and returns a value
async def call_and_wait(value, delay):
    print(f"Calling delayed_print_and_return with value: {value} and delay: {delay}")
    result = await delayed_print_and_return(value, delay)
    print(f"Result from delayed_print_and_return: {result}")
    return result * 2

# Main function to run the tasks
async def main():
    values = [1, 2, 3]
    delays = [1, 2, 3]
    
    # Record the start time for the whole script
    script_start_time = time.time()

    # Create a list of tasks
    tasks = []
    for i in range(len(values)):
        value = values[i]
        delay = delays[i]
        tasks.append(call_and_wait(value, delay))

    # '*' means that the list tasks is being unpacked so that each element of the list is passed as a separate argument to the function.
    # Run the tasks concurrently and wait for them to complete
    results = await asyncio.gather(*tasks)

    # Print the results
    for i in range(len(values)):
        value = values[i]
        result = results[i]
        print(f"Final result for value {value}: {result}")
    
    # Record the end time for the whole script
    script_end_time = time.time()

    # Calculate and print the total time taken for the whole script
    total_time = script_end_time - script_start_time
    print(f"All CPU-bound tasks completed. Total time taken: {total_time} seconds.")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())