# python_http_requests
Python 3 program that uses the Requests module to make the following HTTP requests:

A: A Google search for the term "Tim Berners-Lee".

B: A POST request to a website that does not accept POST requests.

C: A request to a URL that does not exist.

For each request, your program must print:
* The content ("body") of the response
* The status code of the response
* The response headers


## A Google search for the term "Tim Berners-Lee".
*p1.py*
```
/python.exe c:/Users/bhaja/dev/python_http_requests/p1.py


Response url: https://www.google.com/search?q=Tim+Berners-Lee


Response body: <!doctype html><html lang="en"><head><meta charset="UTF-8"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Tim Berners-Lee - Google Search</title><script nonce="f0X-jhGa2HP-ykkYZ7pfXQ">(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"===c||"q"===c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!==document.documentElement;a=a.parentElement)if("A"===a.tagName){a="1"===a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);(function(){
    ...

Soup contents: Tim Berners-Lee - Google SearchGoogle×Please click here if you are not redirected within a few seconds.    AllNewsImagesBooks Maps Videos Shopping Search tools    Any timeAny timePast hourPast 24 hoursPast weekPast monthPast yearAll resultsAll resultsVerbatimTim Berners-LeeComputer scientist · w3.orgView allSir Timothy John Berners-Lee OM KBE FRS FREng FRSA DFBCS, also known as TimBL, is an English computer scientist best known as the inventor of the World Wide Web. He is a Professorial Fellow of Computer Science at the University of Oxford and a... WikipediaBorn: June 8, 1955 (age 67 years), London, United KingdomNationality: BritishAwards: Millennium Technology Prize, Turing Award, The President's Medal, and moreEducation: The Queen's College (1973–1976), Emanuel School (1969–1973), and Sheen Mount Primary SchoolSiblings: Mike Berners-LeeChildren: Ben Berners-Lee and Alice Berners-LeeDates knighted: 1997 and 2004People also askHow did Tim Berners-Lee invent the Internet?What does Tim Berners-Lee do now?Who truly invented the Internet?What was Tim Berners-Lee famous for?Tim Berners-Lee - W3Cwww.w3.org › People › Berners-LeeSir Tim Berners-Lee invented the World Wide Web in 1989. He is the co-founder and CTO of Inrupt.com, a tech start-up which uses, promotes and helps develop the ...Short biography · Talks, articles etcTim Berners-Lee - Wikipediaen.wikipedia.org › wiki › Tim_Berners-LeeSir Timothy John Berners-Lee OM KBE FRS FREng FRSA DFBCS (born 8 June 1955), also known as TimBL, is an English computer scientist best known as the ...Conway Berners-Lee · Mary Lee Woods · Rosemary Leith · MeWeOther names: TimBL; TBLSpouse(s): Nancy Carlson  (m. 1990; div. 2011); Rosemary Leith (m. 2014)Parent(s): Conway Berners-Lee; Mary Lee WoodsBorn: Timothy John Berners-Lee; 8 June 1955 (age 67); London, EnglandSir Tim Berners-Lee - World Wide Web Foundationwebfoundation.org › about › sir-tim-berners-leeThe inventor of the World Wide Web and one of Time Magazine's '100 Most Important People of the 20th Century', Sir Tim Berners-Lee is a scientist and ...Tim Berners-Lee (@timberners_lee) / Twittertwitter.com › timberners_leeTim Cook. Futurology. Raspberry Pi. Stanford University. California Institute of Technology. Physics. Microsoft Windows. Economics. Tim Berners-Lee.Tim Berners-Lee | Biography, Education, Internet ... - Britannicawww.britannica.com › Science › MathematicsAug 26, 2022 · Tim Berners-Lee, in full Sir Tim Berners-Lee, (born June 8, 1955, London, England), British computer scientist, generally credited as the ...Born: June 8, 1955 (age 67) London EnglandInventions: World Wide Web World Wide WebFounder: World Wide Web ConsortiumTim Berners-Lee | Internet Hall of Famewww.internethalloffame.org › inductees › tim-berners-leeIn 1989, Tim Berners-Lee invented the World Wide Web, an Internet-based hypermedia initiative for global information sharing while at CERN, the European ...“I Was Devastated”: Tim Berners-Lee, the Man Who Created the ...www.vanityfair.com › News › tim berners-leeJul 1, 2018 · “I Was Devastated”: Tim Berners-Lee, the Man Who Created the World Wide Web, Has Some Regrets ... Berners-Lee has seen his creation debased by ...Tim Berners-Lee - MIT CSAILwww.csail.mit.edu › person › tim-berners-leeJul 14, 2022 · With a background of system design in real-time communications and text processing software development, in 1989 he invented the World Wide Web, ...The birth of the Web | CERNhome.cern › science › computing › birth-webTim Berners-Lee, a British scientist, invented the World Wide Web (WWW) in 1989, while working at CERN. The web was originally conceived and developed to ...Tim Berners-Lee on 30 years of the world wide web: 'We can get the ...www.theguardian.com › technology › mar › tim-berners-lee-on-30-years-o...Mar 12, 2019 · Tim Berners-Lee on 30 years of the world wide web: 'We can get the web we want'.Related searchesBritish computer scientistAlan TuringCharles BabbageAda LovelaceGeorge BooleMore resultsBritish 
computer scientistTim Berners-Lee net worthTim Berners-Lee ageTim Berners-Lee inventionTim Berners-Lee biographyTim Berners-Lee - WikipediaTim Berners-Lee quotesTim Berners-Lee articleswhen did tim berners-lee die  Next >  Monroe Township, New JerseyFrom your IP address - Learn moreSign inSettingsPrivacyTerms

Response status code: 200

Response header: {'Content-Type': 'text/html; charset=ISO-8859-1', 'Date': 'Tue, 27 Sep 2022 20:05:03 GMT', 'Expires': '-1', 'Cache-Control': 'private, max-age=0', 'Content-Security-Policy': "object-src 'none';base-uri 'self';script-src 'nonce-f0X-jhGa2HP-ykkYZ7pfXQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/xsrp", 'P3P': 'CP="This is not a P3P policy! See g.co/p3phelp for more info."', 'Content-Encoding': 'gzip', 'Server': 'gws', 'X-XSS-Protection': '0', 'X-Frame-Options': 'SAMEORIGIN', 'Set-Cookie': '1P_JAR=2022-09-27-20; expires=Thu, 27-Oct-2022 20:05:03 GMT; path=/; domain=.google.com; Secure, AEC=AakniGPnBRttINYInO8hge-ULX4DN6VSHVz_8w9y1b2SNh200-7bL2exgQ; expires=Sun, 26-Mar-2023 20:05:03 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax, NID=511=urh4Eb2xpF7M9jjSkv4FX9a0rqiUMqG6EuH5UcgsRMfSj4B85KihUBT-YxKML0d-yoErmbm1MuYo0AA41vEi7fPEZtccC2LrzbkW0mpVC3v7sya5QBueS_JFgpXi0HSGTe_ubErkuJ7NaLvzsvThw3F7bje9-6NwKJ23Lt58nZ8; expires=Wed, 29-Mar-2023 20:05:03 GMT; path=/; domain=.google.com; HttpOnly', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"', 'Transfer-Encoding': 'chunked'}
``` 
## A POST request to a website that does not accept POST requests.
*p2.py*
```
$ python.exe p2.py

Response url: https://www.google.com/
Response body: <!DOCTYPE html>
<html lang=en>
  <meta charset=utf-8>
  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
  <title>Error 405 (Method Not Allowed)!!1</title>
  <style>
    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}
  </style>
  <a href=//www.google.com/><span id=logo aria-label=Google></span></a>
  <p><b>405.</b> <ins>That’s an error.</ins>
  <p>The request method <code>POST</code> is inappropriate for the URL <code>/</code>.  <ins>That’s all we know.</ins>

Response status code: 405
Response header: {'Allow': 'GET, HEAD', 'Date': 'Tue, 27 Sep 2022 20:09:25 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Server': 'gws', 'Content-Length': '1589', 'X-XSS-Protection': '0', 'X-Frame-Options': 'SAMEORIGIN', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"'}
```
## A request to a URL that does not exist.
*p3.py*
```
$ python.exe p3.py

Traceback (most recent call last):
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\util\connection.py", line 72, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "C:\Python310\lib\socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\connectionpool.py", line 386, in _make_request
    self._validate_conn(conn)
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\connectionpool.py", line 1042, in _validate_conn
    conn.connect()
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\connection.py", line 358, in connect
    self.sock = conn = self._new_conn()
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSConnection object at 0x0000018CE34911E0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.nonexistentwebsite.com', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000018CE34911E0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:\Users\bhaja\dev\python_http_requests\p3.py", line 3, in <module>
    response = requests.get(url)
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\bhaja\dev\python_http_requests\venv\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='www.nonexistentwebsite.com', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000018CE34911E0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
```