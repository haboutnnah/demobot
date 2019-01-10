from flask import Flask, request

app = Flask(__name__)
SLACKMETHODS = ['GET', 'POST']

@app.route("/", methods=SLACKMETHODS)
def home():
    return "Hello World"

@app.route('/greet', methods=SLACKMETHODS):
def greet():
    return f"hello {request.values.get('text')}"

@app.route('/weather', methods=SLACKMETHODS):
def greet():
    temp = request.values.get('text')
    if int(temp) > 30:
        print("it's so hot")
    else:
        print(f"the temperature is {temp} degrees")


if __name__ == "__main__":
    app.run()
    
