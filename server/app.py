from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:num>')
def count(num):
    output = ''
    for i in range(1, num + 1):
        output += str(i) + '\n'
        return output

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str (num1 * num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str (num1 / num2)
    elif operation == '%':
        return str (num1 % num2)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(debug=True)
    
    