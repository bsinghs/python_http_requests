import requests
url = "https://www.google.com"
response = requests.post(url)
print(response.status_code)
print(response.text)

