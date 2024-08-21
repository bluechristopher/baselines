from flask import Flask, render_template

app = Flask(__name__)

def factorial(n):
    # returns n!
    # n! = 1 * 2 * ... * n, and 0! = 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fib(n):
    # returns the n-th fibonacci number
    # fib(0) = 0, fib(1) = 1, fib(2) = fib(0) + fib(1) = 1, ...
    a = 0
    b = 1
    for i in range(0, n):
        a, b = b, a + b
    return a

@app.route("/")
def home():
    data = []  # to store factorial(n) and fib(n) for n = 0, 1, ...
    for n in range(31):
        data.append((n, factorial(n), fib(n)))  # append a tuple
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=1234)
