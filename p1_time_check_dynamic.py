from bs4 import BeautifulSoup
import requests
import util
import time
start_time = time.time()
url = "https://www.google.com/search"
query = "Tim Berners-Lee"
response = requests.get(url, params={"q": query})
web_request_completed_time = time.time()

util.print_response(response)
# print("Response content: {}".format(response.content))
soup = BeautifulSoup(response.content, 'html.parser')
print("Soup contents: {}".format(soup.text))
parsing_completed_time = time.time()

print("Took %s seconds for web request" % (web_request_completed_time - start_time))
print("Took %s seconds for parsing and printing" % (parsing_completed_time - web_request_completed_time))
print("Took %s seconds total time" % (parsing_completed_time - start_time))

