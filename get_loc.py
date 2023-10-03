import requests
import sys
import os

def get_location(ip, api_key):
    # url for API request
    base_url = f"http://api.ipstack.com/{ip}"
    # parameters to be sent in the API request
    params = {'access_key': api_key}
    # HTTP GET request to the API, passing params, store response
    response = requests.get(base_url, params=params)
    # Check HTTP status if successful
    if response.status_code == 200:
        # Pase the HTTP response in JSON and save it as data
        data = response.json()
        # Check the latitude and longitude presences
        if "latitude" in data and "longitude" in data:
            return data["latitude"], data["longitude"]
        else:
            return None, None
    # Handle different types of error here
    else : 
        print(f"Error: Received status code {response.status_code}")
        return None, None

# for the safety issue, 
if __name__ == "__main__":
    # Check if the ip address provided in command line
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [IP_ADDRESS]")
        sys.exit(1)
    
    ip = sys.argv[1]
    # Obtain the key from local env var
    api_key = os.getenv('IPSTACK_API_KEY')

    # get the location
    lat, longt = get_location(ip, api_key)

    # out put the latitude and longitude
    if lat is not None and longt is not None:
        print(f"Latitude: {lat}, Longitude: {longt}")
    else:
        print("Unable to retrieve the location.")
