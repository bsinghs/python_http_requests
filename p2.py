import requests
import util
url = "https://www.google.com"
response = requests.post(url)
util.print_response(response)

