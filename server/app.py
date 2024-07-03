from flask import Flask, request, render_template # type: ignore

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:param>")
def print_string(param):
    print(param)
    return param

@app.route("/count/<int:param>")
def count(param):
    return "<br>".join(str(i) for i in range(param))

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
       