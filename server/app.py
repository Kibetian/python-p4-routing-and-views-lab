from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the string to the console
    return f"<p>Printed String: {param}</p>"

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(1, param + 1))
    return f"<p>Counting numbers from 1 to {param}:</p><pre>{numbers}</pre>"

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f"<p>{num1} {operation} {num2} = {result}</p>"
    else:
        return "Invalid operation."

if __name__ == '__main__':
    app.run(debug=True)
