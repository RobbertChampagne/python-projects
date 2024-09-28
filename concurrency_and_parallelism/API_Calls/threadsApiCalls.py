# python concurrency_and_parallelism/API_Calls/threadsApiCalls.py

# Demonstrates how to use threads to make concurrent API calls using the httpx library in Python. 
# This example will fetch data from a public API concurrently using multiple threads.

import threading
import httpx
import time

# Function to make an API call
def fetch_data(url):
    response = httpx.get(url)
    if response.status_code == 200:
        print(f"Data from {url}: {response.json()}")
    else:
        print(f"Failed to fetch data from {url}")

# Worker function for threading
def worker(url):
    fetch_data(url)

# List of URLs to fetch data from
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4"
]

# Record the start time for the whole script
script_start_time = time.time()

# Create and start threads
threads = []
for url in urls:
    thread = threading.Thread(target=worker, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Record the end time for the whole script
script_end_time = time.time()

# Calculate and print the total time taken for the whole script
total_time = script_end_time - script_start_time
print(f"All API calls completed. Total time taken: {total_time} seconds.")