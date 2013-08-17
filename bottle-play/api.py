#!/usr/bin/env python
from time import sleep
from bottle import route, run, request, HTTPResponse

@route("/")
def hello():
    return "Hello client\n"

@route("/multiply/:a/:b")
def multiply(a=0, b=0):
    if not is_int(a) or not is_int(b):
        raise HTTPResponse(status=400, output="We only support ints")
    return str(int(a)*int(b))


@route("/echo", method="POST")
@route("/echo/", method="POST")
def echo():
    sleep(0.05)
    return request.body.read()

def is_int(num):
    try:
        int(num)
    except ValueError:
        return False
    return True

run(port=8080, debug=True, reloader=True)
