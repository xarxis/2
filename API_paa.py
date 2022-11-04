#работа с API
import requests
import json
endpoint_device = 'https://api.openweathermap.org/data/2.5/weather?lat={55.75396}&lon={37.620393}&appid={3cf93a35ad6a33e3cf94a69e010041dd}'
headers = {'X-Yandex-API-Key': '7db1ea84-a07c-4bfc-937a-bf45c29adca0'}
r_dev = requests.get(endpoint_device, headers=headers, verify=False)
#print(type(r_dev))
j_dev = json.loads(r_dev.text)
#print(json.dumps(j_dev, indent=4))
#print(type(j_dev))
t=j_dev["fact"]["condition"]
print(t)
with open('weather.json', 'w') as f:
    json.dump(j_dev, f)

