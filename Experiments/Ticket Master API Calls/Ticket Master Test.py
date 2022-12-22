import requests
import json

def retrieve_tm_events():
    url = 'https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&apikey=8jmQq5KG054syjOihuIyX3rFGyghM0Oe'

    header={
        "Accept": "application/json"
    }

    response = requests.get(
        url,
        headers=header
    )

    tm_events_data = response.json()['_embedded']['events']
    # print(type(tm_events_data))
    tm_events_dict = {}
    
    for events in tm_events_data:
        tm_events_dict[events['name']] = events['sales']['public']['startDateTime']
        # tm_events_dict[events['name']] = events['name']
        # tm_events_dict[events['sales']['public']['startDateTime']] = events['sales']['public']['startDateTime']
        # tm_events_dict["Name"] = events['name']
        # tm_events_dict["Sales Start Date"] = events['sales']['public']['startDateTime']

    for name,sales in tm_events_dict.items():
        print(f"Name:  {name}\nSales: {sales}")
        # print(f"Sales: {sales}")

if __name__ == '__main__':
    retrieve_tm_events()


    # for device in device_list:
    #     parsed_data[device['name']] = device['site']['name']

    # for k,v in parsed_data.items():
    #     print(f"{k}: {v}")