import requests

url = "https://raw.githubusercontent.com/poornima822/my-first-repo/refs/heads/main/hello.py"
response = requests.get(url)

if response.status_code == 300:
    print(response.text)
else:
    print(f"Failed to fetch the script. Status code: {response.status_code}")
