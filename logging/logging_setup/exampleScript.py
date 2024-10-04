# python logging/logging_setup/exampleScript.py

import httpx
from loggingSetup import setup_logging
import logging
import asyncio

async def get_user():
    # Create an asynchronous HTTP client
    async with httpx.AsyncClient() as client:
        # Construct the URL for the API endpoint
        url = "https://reqres.in/api/users/8"
            
        # Make an asynchronous GET request to the API
        response = await client.get(url)
            
        # Assert that the response status code is 200 (OK)
        assert response.status_code == 200

        # Extract the user data from the JSON response
        user = response.json()["data"]
            
        # Assert that the user data is a dictionary
        assert isinstance(user, dict)


def main():
    
    # Initialize logging
    setup_logging()
    
    # Run the get_user coroutine
    asyncio.run(get_user())
    
    logging.info("Logging example.")


if __name__ == '__main__':
    main()