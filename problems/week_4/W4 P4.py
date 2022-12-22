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

    device_list = response.json()['results']
    print(type(device_list))
    for device in device_list:
        # print(device['id'])
        # print(device['device_type']['manufacturer']['display'])
        print(f"{device['display']}: {device['site']['name']}")
    
    # with open('json_data.json', 'w') as outfile:
        # for key, value in device_list.items():
        #     outfile.write('%s:%s\n' % (key, value))
    
    # return json.dumps(device_list, indent=4)

get_device_list()