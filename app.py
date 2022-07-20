from flask import Flask
from math import sqrt


app = Flask(__name__)


def is_prime(number):
    is_num_prime = True

    for i in range(2, round(sqrt(number)) + 1):
        if number % i == 0:
            is_num_prime = False
            break

    return is_num_prime


def get_prime_list(limit_number):
    return [i for i in range(2, limit_number + 1) if is_prime(i)]


@app.route("/list-prime/<num>")
def list_primes(num):
    return get_prime_list(num)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
