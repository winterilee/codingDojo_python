from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/success')
def success():
    return 'Success'

@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    return f"Hello {name * num}"

if __name__ == "__main__":
    app.run(debug = True, port = 5001)
