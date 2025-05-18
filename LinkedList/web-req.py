import time
import requests

# URL of the website you want to visit
url = 'https://github.com/shadmansshuvo'

while True:
    # Send an HTTP GET request to the website
    response = requests.get(url)
    
    # Print the status code (optional, just to see the result)
    print(f"Status Code: {response.status_code}")
    
    # Wait for 1 second before sending the next request
    time.sleep(1)