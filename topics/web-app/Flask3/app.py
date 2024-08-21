from flask import Flask, render_template

app = Flask(__name__)

def fib(n):
    # recursive version (highly inefficient, exponential time complexity)
    if n <= 1:  # base case, fib(0) = 0, fib(1) = 1
        return n
    else:  # recursive case
        return fib(n - 1) + fib(n - 2)

def factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(str(i))
    return ", ".join(factors)

@app.route("/")
def home():
    data = []  # to store factorial(n) and fib(n) for n = 0, 1, ...
    for n in range(21):
        data.append((n, fib(n), factors(fib(n))))
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=1234)
