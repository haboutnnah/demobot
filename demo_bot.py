"""
is demo bot
"""

from flask import Flask, request

app : Flask = Flask(__name__)
SLACKMETHODS = ['GET', 'POST']

@app.route("/", methods=SLACKMETHODS)
def home() -> str:
    return "Hello World"

@app.route('/greet', methods=SLACKMETHODS)
def greet() -> str:
    return f"hello {request.values.get('text')}"

@app.route('/weather', methods=SLACKMETHODS)
def weather() -> str:
    temp = request.values.get('text')
    if int(temp) > 30:
        print("it's so hot")
    else:
        print(f"the temperature is {temp} degrees")


if __name__ == "__main__":
    app.run(debug=True)   
