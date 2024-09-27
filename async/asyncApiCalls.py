# python async/asyncApiCalls.py

# The use of asyncio allows for efficient non-blocking I/O operations,
# making the code more performant compared to using threads for I/O-bound tasks.

import asyncio
import httpx

# Asynchronous function to make an API call
async def fetch_data(client, url):
    response = await client.get(url)
    if response.status_code == 200:
        print(f"Data from {url}: {response.json()}")
    else:
        print(f"Failed to fetch data from {url}")

# Main function to run the tasks
# it is a common and recommended practice to encapsulate your asynchronous code within a main function 
# for better organization and readability. 
# This also helps to ensure that the asynchronous code is only executed when the script is run directly, 
# not when it is imported as a module.

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4"
    ]

    async with httpx.AsyncClient() as client:
        tasks = [fetch_data(client, url) for url in urls] # Creates a list of tasks (coroutines) to be executed concurrently.
        
        # '*' means that the list tasks is being unpacked so that each element of the list is passed as a separate argument to the function.
        await asyncio.gather(*tasks) # To run the tasks concurrently and wait for all of them to complete.

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())

print("All API calls completed.")