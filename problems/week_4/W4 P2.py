import requests
# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# r.status_code
# r.headers['content-type']
# r.encoding
# r.text
# r.json()

sunrise_sunset = requests.get('https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400')
print(sunrise_sunset.status_code)
print(sunrise_sunset.headers['content-type'])
print(sunrise_sunset.encoding)
print(sunrise_sunset.text)
print(sunrise_sunset.json())
print(sunrise_sunset)