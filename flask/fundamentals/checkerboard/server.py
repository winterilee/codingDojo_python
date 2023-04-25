from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", num_x = 8, num_y = 8, color_1 = "black", color_2 = "red")

@app.route('/<int:x>')
def columns(x):
    return render_template("index.html", num_x = x, num_y = 8, color_1 = "black", color_2 = "red")

@app.route('/<int:x>/<int:y>')
def axis(x, y):
    return render_template("index.html", num_x = x, num_y = y, color_1 = "black", color_2 = "red")

@app.route('/<int:x>/<int:y>/<string:c1>')
def color(x, y, c1):
    return render_template("index.html", num_x = x, num_y = y, color_1 = c1, color_2 = "red")

@app.route('/<int:x>/<int:y>/<string:c1>/<string:c2>')
def colors(x, y, c1, c2):
    return render_template("index.html", num_x = x, num_y = y, color_1 = c1, color_2 = c2)

if __name__ == "__main__":
    app.run(debug = True, port = 5001)