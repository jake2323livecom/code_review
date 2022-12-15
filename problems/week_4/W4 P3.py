import requests
import json

def get_device_list():

    ''' Returns the current device list for the Nautobot demo website '''

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

    device_list = response.json()

    return json.dumps(device_list, indent=4)


print(get_device_list())