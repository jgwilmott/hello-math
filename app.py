import random
from flask import Flask, render_template

app = Flask(__name__)

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route("/")
def hello_world():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    return render_template("hello.html", sum = "" + str(x) + " + " + str(y) + " = " + str(x + y))

