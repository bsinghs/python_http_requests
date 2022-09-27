import requests
import util
url = "https://www.nonexistentwebsite.com"
response = requests.get(url)
util.print_response(response)

