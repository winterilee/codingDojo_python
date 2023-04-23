from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", num = 0)

@app.route('/play')
def play():
    return render_template("index.html", num = 3, color = "cornflowerblue")

@app.route('/play/<int:num>')
def play_num(num):
    return render_template("index.html", num = num, color = "cornflowerblue")

@app.route('/play/<int:num>/<string:color>')
def play_all(num, color):
    return render_template("index.html", num = num, color = color)

if __name__ == "__main__":
    app.run(debug = True, port = 5001)