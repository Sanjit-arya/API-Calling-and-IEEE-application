import requests
response = requests.get('https://ieeerecruitment.shivzee.in/api/v1')
data = response.json()
print(data)