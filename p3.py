import requests
url = "https://www.nonexistentwebsite.com"
response = requests.get(url)
print(response.status_code)
print(response.text)

