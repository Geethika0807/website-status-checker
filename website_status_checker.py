import requests
websites=[
    "https://www.google.com",
    "https://www.openai.com",
    "https://www.github.com"
]
for website in websites:
    try:
        response=requests.get(website)
        if response.status_code==200:
            print(f"{website} --> Online ✅")
        else:
            print(f"{website}--> Status code: {response.status_code}")
    except Exception as e:
        print(f"{website}--> Offline ❌")