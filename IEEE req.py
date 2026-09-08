import requests

url = "https://ieeerecruitment.shivzee.in/api/v1/auth/login"

data = {
    "email": "sanjitarya.s2026@vitstudent.ac.in",
    "password": "Greatboy7!"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.text)
data = response.json()
print(data)
token = data['token']
print(token)

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://ieeerecruitment.shivzee.in/api/v1/questions?dept=technical"

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)

questions = response.json()
for q in questions:
    print(q['id'])
    print(q['body'])
    print(q['title'])
    print()

#answers = [
    #"question-id":"291e85a7-86d6-49ae-b862-00733f65a09d","body":""
#]


