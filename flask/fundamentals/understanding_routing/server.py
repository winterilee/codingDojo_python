from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:phrase>')
def say(phrase):
    return f"Hi {phrase}!"

@app.route('/repeat/<int:num>/<string:phrase>')
def repeat(num, phrase):
    return f"{phrase} " * num

if __name__ == "__main__":
    app.run(debug = True, port = 5001)
