# python concurrency_and_parallelism/asyncio/concurrency.py

import asyncio

# Asynchronous function that simulates a computation and returns a value
async def compute_square(number):
    print(f"Computing square of {number}...")
    await asyncio.sleep(1)  # Simulate a delay
    result = number * number
    print(f"Square of {number} is {result}")
    return result

# Asynchronous function that simulates a computation and returns a value
async def compute_cube(number):
    print(f"Computing cube of {number}...")
    await asyncio.sleep(1.5)  # Simulate a longer delay
    result = number * number * number
    print(f"Cube of {number} is {result}")
    return result

# Asynchronous function that combines the results of other computations
async def compute_square_and_cube(number):
    square = await compute_square(number)
    cube = await compute_cube(number)
    return square, cube

# Main function to run the tasks
async def main():
    numbers = [2, 3, 4]

    # Create a list of tasks
    tasks = [compute_square_and_cube(number) for number in numbers]

    # Run the tasks concurrently and wait for them to complete
    results = await asyncio.gather(*tasks)

    # Print the results
    for number, (square, cube) in zip(numbers, results):
        print(f"Number: {number}, Square: {square}, Cube: {cube}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())