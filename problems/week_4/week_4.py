import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings()


##################################################################################
##################################################################################
##################################################################################


# def get_auth_token():

#     ''' Returns the authentication token for the Cisco DNAC Sandbox '''

#     url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

#     response = requests.post(
#         url,
#         auth=HTTPBasicAuth(
#             username="devnetuser",
#             password="Cisco123!"
#             ), 
#         verify=False,
#     )

#     token = response.json()
  
#     return token

# if __name__ == "__main__":
#     print(get_auth_token())


##################################################################################
##################################################################################
##################################################################################


def get_device_list():

    ''' Returns the current device list for the Nautobot demo website '''

    url = "https://demo.nautobot.com/api/dcim/devices/"
    token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    headers={
            "Authorization": "Bearer Token {}".format(token),
            "Accept": "application/json; indent=4"
    }

    response = requests.get(
        url,
        auth=HTTPBasicAuth(
            username="demo",
            password="nautobot",
            ),
        headers=headers,
        verify=False
    )

    device_list = response.json()

    return device_list

if __name__ == "__main__":
    print(get_device_list())

print(__name__)


# curl -H "Authorization: Token aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
# -H "Accept: application/json; indent=4" \
# https://demo.nautobot.com/api/dcim/devices/