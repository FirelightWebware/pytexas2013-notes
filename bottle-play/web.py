#!/usr/bin/env python
from bottle import route, run, template, static_file, request
import requests


@route("/public/<filename:path>")
def send_static(filename):
    return static_file(filename, root="./public")


@route("/")
@route("/", method="POST")
def multiply():
    a = request.forms.get('a')
    b = request.forms.get('b')
    if a and b:
        greeting = requests.get(
            "http://localhost:8080/multiply/{}/{}" \
            .format(a, b)
        ).content
    else:
        greeting = "multiply some numbers"
    return template("multiply", greeting=greeting)


run(port=8081, debug=True, reloader=True)
