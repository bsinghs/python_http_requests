def print_response(response):
    print("Response url: {}".format(response.url))
    print("Response body: {}".format(response.text))
    print("Response status code: {}".format(response.status_code))
    print("Response header: {}".format(response.headers))
