# flask app
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello World  !"

@app.route("/about")
def about():
    return "<h1 style='color: turquoise'> MORE  About !!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    