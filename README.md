# Geolocation IP Lookup CLI

## Description

A simple command-line interface application developed in Python that fetches and displays the geolocation of an IP address using the IPStack API.

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
python3 get_location.py [IP_ADDRESS]
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











