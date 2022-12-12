import requests
from requests.auth import HTTPBasicAuth

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
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": None,
        #     "Accept": "application/json"
        # }
    )

    token = response.json()

    # print(token)
   
    return token

if __name__ == "__main__":
    print(get_auth_token())