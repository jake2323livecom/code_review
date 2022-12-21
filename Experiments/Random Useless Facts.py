import requests
import json

def retrieve_useless_fact():
    '''Retrieves and displays a useless fact from the site uselessfacts.jsph.pl'''
    url = 'https://uselessfacts.jsph.pl/random.json?language=en'

    header={
        "Accept": "application/json"
    }

    response = requests.get(
        url,
        headers=header,
        # verify=False
    )

    useless_fact_data = response.json()

    useless_fact = useless_fact_data['text']
    
    return useless_fact

if __name__ == '__main__':
    print(retrieve_useless_fact())