import requests
import json

def device_map():

    url = "https://demo.nautobot.com/api/dcim/devices/"

    token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    headers={
            "Authorization": "Token {}".format(token),
            "Accept": "application/json"
    }

    response = requests.get(
        url,
        headers=headers,
        verify=False
    )

    device_list = response.json()['results']
    
    parsed_data = {}
    
    # device = device_list

    for device in device_list:
        parsed_data[device['name']] = device['site']['name']

    for k,v in parsed_data.items():
        print(f"{k}: {v}")

device_map()