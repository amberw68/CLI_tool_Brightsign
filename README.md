# Geolocation IP Lookup CLI

## Description

A simple command-line interface application developed in Python that fetches and displays the geolocation of an IP address using the IPStack API.

### API Request:

- The function get_location(ip, api_key) constructs an API request URL using the provided IP address.
- Utilizing the requests library, it sends an HTTP GET request to the IPStack API with the user's API key as a parameter.

### Response Handling:

- It checks the HTTP status code to ensure the request was successful (status_code == 200). If unsuccessful, it outputs an error message with the received status code.
- If successful, it parses the JSON response to extract and return the latitude and longitude values. If these values are not present, it returns None.

### CL Interaction:

- It checks the valid argument input (target IP address)
- It retrieves the IPStack API key from the pre-set env var to avoid hard-coding caused security concern

### Output:

- The latitude and longitude are printed to the std output in a readable format. 
- If the not location information is not in JSON data, the error message would be displayed. 

## Prerequisites

- Python 3.x (tested on Python 3.6.9)
- An API Key from IPStack ([Get here](https://ipstack.com/))

## Installation & Setup

### Clone the Repository:

```bash
git clone https://github.com/amberw68/CLI_tool_Brightsign.git
cd CLI_tool_Brightsign/
```

### API Key Configuration
Replace 'your_api_key' with your actual API key.
```bash
export IPSTACK_API_KEY='your_api_key'
```

## Usage
Replace [IP_ADDRESS] with target ip address.
```bash
python3 get_loc.py [IP_ADDRESS]
```

## Docker Usage
If you prefer to use Docker, you can build and run the application as a Docker container.

### Build the Docker Image
```bash 
docker build -t geolocation-ip-lookup .
```
### Run the Docker Container (Replace 'your_api_key' with your actual API key. Replace [IP_ADDRESS] with target ip address.)
```bash
docker run --rm -e IPSTACK_API_KEY='your_api_key' geolocation-ip-lookup [IP_ADDRESS]
```











