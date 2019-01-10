"""
is demo bot
"""

from flask import Flask, request
import random

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
    return f"A random number between one and ten is {random.randint(1,10)}"

if __name__ == "__main__":
    app.run(debug=True)  
