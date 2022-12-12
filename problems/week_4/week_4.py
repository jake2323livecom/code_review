import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()
import json


##################################################################################
##################################################################################
##################################################################################


def get_auth_token():

    ''' Returns the authentication token for the Cisco DNAC Sandbox '''

    url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

    response = requests.post(
        url,
        auth=HTTPBasicAuth(
            username="devnetuser",
            password="Cisco123!"
            ), 
        verify=False,
    )

    token = response.json()
  
    return token

print(get_auth_token())


##################################################################################
##################################################################################
##################################################################################


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


##################################################################################
##################################################################################
##################################################################################


