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
        return("it's so hot")
    else:
        return(f"the temperature is {temp} degrees")

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
    returns pi to n decimal places
    """
    text = request.values.get('text')
    print(int)
    #try:
    dec_places = int(text)
    return dec_places
    #except ValueError:
    #    return 'lmao follow the instructions pls'
    #mp.dps = dec_places
    #return mp.pi

if __name__ == "__main__":
    app.run(debug=True)  
