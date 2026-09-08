import requests

url = "https://ieeerecruitment.shivzee.in/api/v1/auth/login"

data = {
    "email": "placeholder",
    "password": "placeholder"
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

answers = [
    {"question_id":"291e85a7-86d6-49ae-b862-00733f65a09d","body":" When I was starting with python, there was a simple problem, ‘Find the largest among three numbers’, which I tried to solve using nested if/elif statements. Everytime i tried an edge case, countless errors occurred, sometimes it didn’t print an output or the output was wrong. I realised the approach itself was wrong, and implemented a champion variable to check ‘the largest so far’. As a beginner, the way to approach problems in a multitude of ways intrigued me and it was the moment that made me fall in love with problem-solving. "},
    {"question_id":"70f7e96b-2c3f-4680-99e3-24805366131e","body":"I picked up Git about 2 weeks ago to prepare for a hackathon. Learning Git changed the way I think about teamwork in coding. With Git, conflicts are shown clearly and everyone can work on their own branch. I deliberately have practiced creating merge conflicts on purpose with my teammates. In a collaborative project, I would want every teammate to commit early and work on their own branches, merging into main only once it’s tested."},
    {"question_id":"f0c4f0ac-9cde-42f1-bdb1-c4374bdae348","body":"I’d start by reading the error logs and try to point out the cause. Using test cases, I’d try to create the crash again and find specifically what is triggering the crash. If I couldn’t find and fix the cause, I’d publish a smaller and stable version of the site."},
    {"question_id":"7549ed35-1a03-4d63-b2fb-43484aad7847","body":"First, I would revert to the last working version, because that would calm the team down after they see a working demo, even with fewer features. Then, I’d ask the team to gather and talk about what caused it without singling out any teammate."},
    {"question_id":"11841e04-91ac-4ba7-8ded-00a7222dddf5","body":"I’m still fairly new, I haven’t really worked on a large project yet and don’t really follow programming constructs. However, I have inculcated a few habits while coding :- Testing boundary cases, understanding code before using it (like through flowcharts and writing down the logic) and naming variables clearly, which is pretty standard practice."},
    {"question_id":"6ee9fc54-987d-49bd-86cb-3ad735dba062","body":"I would love to explore neural networks and on how to build it with raw maths and python, without the use of python libraries like PyTorch or TensorFlow, and am currently striving to try to make one from scratch. It requires a lot of prerequisite knowledge I don’t fully have yet, but that’s part of what makes it exciting."},
    {"question_id":"f0df8691-b3c4-49dd-81d1-5f9a8fc3b613","body":"Python was my first language and of course the first thing I did was print “Hello World!”. I first encountered the language, I was fascinated how a computer could think, understand my instructions and return an output onto the screen. Using Python, of course I built this application for IEEE compsoc by learning API calling."},
    {"question_id":"9996086d-0224-4ae4-9495-1aef26744d92","body":"I talked to seniors at the club expo and came to realise this club doesn’t only focus on the technical aspects, but we also get to experience different social elements to like meeting new people and just having a fun community in general. (If it helps I can supply more white monster cans for building swords :). )"},
    {"question_id":"536cfe39-cab2-45ce-a3e6-77731406d195","body":"Github:https://github.com/Sanjit-arya Linkedin: https://www.linkedin.com/in/sanjit-arya/"}
]

body = {"answers": answers}

save_url = "https://ieeerecruitment.shivzee.in/api/v1/applications/918e372f-05cf-4503-acf0-87e50c8098ab/save"

response = requests.patch(save_url, json=body, headers=headers)
print(response.status_code)
print(response.text)

response = requests.patch(save_url, json=body, headers=headers)
print(response.status_code)
print(response.text)

if response.status_code == 200:
    submit_url = f"https://ieeerecruitment.shivzee.in/api/v1/applications/918e372f-05cf-4503-acf0-87e50c8098ab/submit"
    
    submit_response = requests.post(submit_url, headers=headers)
    print(submit_response.status_code)
    print(submit_response.text)
    
    if submit_response.status_code == 200:
        print("Application submitted successfully")
    else:
        print("Submit failed")
else:
    print("Save failed")


