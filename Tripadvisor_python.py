import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal',
    'url': 'https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html',
    'user_agent_type': 'desktop',
    'geo_location': 'United States'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),
    json=payload
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())