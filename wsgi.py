import os
import urllib.request


def printrole(environ, start_response):
    podname = os.environ["HOSTNAME"]
    if determinemaster():
        response = "role:leader,podname:"+podname
        response_body = response.encode(encoding="utf-8")
    else:
        response = "role:slave,podname:"+podname
        response_body = response.encode(encoding="utf-8")
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return iter([response_body])


def determinemaster():
    podname = os.environ["HOSTNAME"]
    with urllib.request.urlopen('http://localhost:4040') as response:
        html = response.read().decode()
        leaderpodname = html.split('"')[3]
    return podname == leaderpodname
