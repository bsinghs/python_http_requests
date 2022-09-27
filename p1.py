from bs4 import BeautifulSoup
import requests
import util
url = "https://www.google.com/search"
query = "Tim Berners-Lee"
response = requests.get(url, params={"q": query})
util.print_response(response)
# print("Response content: {}".format(response.content))
soup = BeautifulSoup(response.content, 'html.parser')
print("Soup contents: {}".format(soup.text))