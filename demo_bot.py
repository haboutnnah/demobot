"""
is demo bot
"""

from flask import Flask, request
import random
from mpmath import mp

app: Flask = Flask(__name__)
SLACKMETHODS = ['GET', 'POST']

@app.route("/", methods=SLACKMETHODS)
def home() -> str:
    """
    test
    """
    return "Hello World"

@app.route('/greet', methods=SLACKMETHODS)
def greet() -> str:
    """
    greets user
    """
    return f"hello {request.values.get('text')}"

@app.route('/weather', methods=SLACKMETHODS)
def weather() -> str:
    """
    returns temp
    """
    temp = request.values.get('text')
    if int(temp) > 30:
        print("it's so hot")
    else:
        print(f"the temperature is {temp} degrees")

@app.route('/random', methods=SLACKMETHODS)
def randomint() -> str:
    """
    returns a random int between 1 and 10
    """
    minimum: int = 1
    maximum: int = 10
    return f"A random number between {minimum} and {maximum} is {random.randint(minimum,maximum)}"

@app.route('/pi', methods=SLACKMETHODS)
def pi_to_dec_places() -> str:
    """
    returns a random int between 1 and 10
    """
    try:
        dp = int(request.values.get('text'))
    except expression as identifier:
        pass
    minimum: int = 1
    maximum: int = 10
    return f"A random number between {minimum} and {maximum} is {random.randint(minimum,maximum)}"

if __name__ == "__main__":
    app.run(debug=True)  
